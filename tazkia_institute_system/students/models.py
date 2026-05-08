from django.db import models
from accounts.models import Parent

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male','ذكر'),('female','أنثى')])
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name='students')
    health_status = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.full_name
