from django.db import models
import json

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()

    character_score = models.FloatField(default=100)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
    
class StudentFace(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="faces"
    )

    image = models.ImageField(upload_to='student_faces/')

    encoding = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Face Image of {self.student.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

