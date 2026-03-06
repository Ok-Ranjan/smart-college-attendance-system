# Image Upload System in Django

In this project, students upload face images during registration.

Django stores uploaded files using ImageField.

Example model field:

    face_image = models.ImageField(upload_to='student_faces/')

## How Image Storage Works

1. User uploads image
2. Django receives file
3. Pillow library validates the image
4. Image is stored in MEDIA_ROOT folder
5. Database stores only the file path

Example database value:

    student_faces/student1.jpg

Actual file location:

    media/student_faces/student1.jpg