from django import forms
from .models import Student, StudentFace

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll_number', 'branch', 'year']
    

class StudentFaceForm(forms.ModelForm):
    class Meta:
        model = StudentFace
        fields = ['image']
