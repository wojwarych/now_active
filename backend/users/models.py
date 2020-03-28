from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=32, blank=True)

    constraints = [
        models.UniqueConstraint(
            fields=["phone_number", "name", "last_name"],
            name="unique phone_number",
        )
    ]

    def __str__(self):
        return (
            f'{self.name} {self.last_name}. Phone number: {self.phone_number}'
        )


DAYS = (
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
    ('SU', 'Sunday'),
)


class Trainer(User):
    available_days = ArrayField(
        models.CharField(max_length=2, choices=DAYS), size=7, default=list
    )
