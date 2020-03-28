from django.db import models

from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_payments'
    )
    value = models.DecimalField(max_digits=4, decimal_places=2)
    deadline = models.DateField()

    constraints = models.UniqueConstraint(
        fields=['user', 'deadline'], name='user_deadline_constraint'
    )

    def __str__(self):
        return f'User {self.user} payment of {self.value} to {self.deadline}'
