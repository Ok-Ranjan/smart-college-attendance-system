from django.db import models
from accounts.models import Student, Teacher
# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    

