from django.db import models
from students.models import Student
from circles.models import Circle
from accounts.models import Teacher

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject_or_part = models.CharField(max_length=150)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    evaluation = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    date = models.DateField()
