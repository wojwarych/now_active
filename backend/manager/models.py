from django.db import models

from users.models import Trainer, User

PLAYERS_LEVELS = (("B", "Beginner"), ("I", "Intermediate"), ("A", "Advanced"))


class PlayersClass(models.Model):
    level = models.CharField(max_length=1, choices=PLAYERS_LEVELS)
    players = models.ManyToManyField(User, related_name="class_students")
    training_place = models.OneToOneField(
        "TrainingPlace", on_delete=models.CASCADE
    )
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="trainer_classes"
    )
    training_date = models.DateTimeField()


def __str__(self):
    return f'Class {self.level} at {self.training_place} with {self.trainer}'


class TrainingPlace(models.Model):
    name = models.CharField(max_length=64, blank=False)
    city = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=64, null=False, blank=False)
    open_from = models.DateTimeField()
    closed_at = models.DateTimeField()
    trainer = models.ManyToManyField(
        Trainer, related_name="trainings_trainers"
    )

    @property
    def full_address(self):
        return f"{self.city} {self.address}"

    @property
    def working_hours(self):
        return (self.open_from, self.closed_at)

    def __str__(self):
        return f"{self.name} in {self.city} {self.address}"
