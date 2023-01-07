from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)