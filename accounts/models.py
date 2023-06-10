from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):

    """Custom User model extends a pre-defined django AbstractUser model"""

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, max_length=255)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
