from django.db import models

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
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

