from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to="tweets/photos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.user.username}: {self.content[:20]}..."
