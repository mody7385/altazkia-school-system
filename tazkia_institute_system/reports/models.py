from django.db import models
from accounts.models import User

class Report(models.Model):
    title = models.CharField(max_length=150)
    report_type = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    file = models.FileField(upload_to='reports/', blank=True, null=True)
    generated_content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
