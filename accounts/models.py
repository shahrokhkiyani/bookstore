from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):  # username, firstname, lastname, email, password, ..., Age
    age = models.PositiveIntegerField(null=True, blank=True)
