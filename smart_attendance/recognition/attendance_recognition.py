import face_recognition
import json
import numpy as np

from  accounts.models import StudentFace

def recognize_students(image_path):

    # Load the teacher's uploaded classroom photo
    image = face_recognition.load_image_file(image_path)

    # detect the faces: tells the system where each face is located
    face_locations = face_recognition.face_locations(image)

    # convert faces to encodings: each face becomes a 128-number bector
    face_encodings = face_recognition.face_encodings(image, face_locations)

    recognized_students = []

    # Load all student encodingg
    student_faces = StudentFace.objects.all()

    known_encodings = []
    student_ids = []

    for face in student_faces:
        
        encoding = json.loads(face.encoding)

        known_encodings.append(np.array(encoding))

        student_ids.append(face.student.id)

    # compare each detected face
    for face_encoding in face_encodings:
        
        matches = face_recognition.compare_faces(known_encodings, face_encoding)

        if True in matches:

            index = matches.index(True)

            recognized_students.append(student_ids[index])
    
    return recognized_students