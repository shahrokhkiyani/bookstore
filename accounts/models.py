from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # username, firstname, lastname, email, password, ..., Age
    age = models.PositiveIntegerField()