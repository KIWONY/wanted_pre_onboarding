from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username