from django.db import models
from accounts.models import Teacher, Supervisor
from students.models import Student

class Circle(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='circles')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, related_name='circles')
    students = models.ManyToManyField(Student, blank=True, related_name='circles')
    level = models.CharField(max_length=100, blank=True)
    schedule = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
