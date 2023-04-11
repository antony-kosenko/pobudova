from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    online = models.BooleanField(null=False, default=False)
