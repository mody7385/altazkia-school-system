from django.db import models
from students.models import Student
from circles.models import Circle
from accounts.models import Teacher

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present','حاضر'),('absent','غائب'),('late','متأخر')])
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
