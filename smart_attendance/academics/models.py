from django.db import models
from accounts.models import Student
# Create your models here.

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    marks = models.FloatField(default=0)

    submitted = models.BooleanField(default=False)


class Activity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    activity_name = models.CharField(max_length=200)

    points = models.FloatField(default=0)

