from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return f"{self.username}"

