from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'مدير'
        SUPERVISOR = 'supervisor', 'مشرف'
        TEACHER = 'teacher', 'معلم'
        PARENT = 'parent', 'ولي أمر'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PARENT)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    relation_to_student = models.CharField(max_length=100, default='ولي أمر')
    def __str__(self): return self.full_name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor_profile')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
