from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
