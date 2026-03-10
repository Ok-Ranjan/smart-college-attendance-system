from django.shortcuts import render, redirect
from .forms import StudentForm, StudentFaceForm
from .models import Student
from recognition.face_encoding import generate_face_encoding
import json

# Create your views here.

def register_student(request):

    if request.method == "POST":

        student_form = StudentForm(request.POST)
        face_form = StudentFaceForm(request.POST, request.FILES)

        if student_form.is_valid() and face_form.is_valid():

            student = student_form.save()

            face = face_form.save(commit=False)
            face.student = student
            face.save()

            # generate encodinf
            encoding = generate_face_encoding(face.image.path)

            if encoding is not None:
                face.encoding = json.dumps(encoding.tolist())
                face.save()
            
            return redirect("admin:index")
        
    else:

        student_form = StudentForm()
        face_form = StudentFaceForm()
    
    return render(request, "accounts/register_student.html", {
        "student_form": student_form,
        "face_form": face_form
    })