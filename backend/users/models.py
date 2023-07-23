from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Здесь вы можете добавить дополнительные поля для пользователя, если необходимо
    pass