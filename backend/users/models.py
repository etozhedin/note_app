from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar_url = models.URLField(max_length = 200, default=None, null=True)