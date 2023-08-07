from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, default=None)
