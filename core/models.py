from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    """
    A custom user profile model that extends Django's AbstractUser.
    This model adds a role field to distinguish between patients and doctors 
    in the system.
    """

    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return f"{self.username} ({self.role})"
