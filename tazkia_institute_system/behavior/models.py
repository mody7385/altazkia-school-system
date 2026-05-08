from django.db import models
from students.models import Student
from accounts.models import User

class BehaviorRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20, choices=[('warning','إنذار'),('violation','مخالفة'),('commitment','تعهد')])
    title = models.CharField(max_length=150)
    description = models.TextField()
    parent_notified = models.BooleanField(default=False)
    date = models.DateField()
