from django.db import models
from accounts.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outbox_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox_messages')
    subject = models.CharField(max_length=150)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
