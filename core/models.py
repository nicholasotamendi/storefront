from django.contrib.auth.models import AbstractUser
from django.db import models


# THis class is used by django to create a user module that takes email as a unique field
class User(AbstractUser):
    email = models.EmailField(unique=True)