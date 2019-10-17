from django.db import models
from datetime import date
from apps.logRegApp.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments")
    message = models.ForeignKey(Message, related_name="comments")
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

