from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
