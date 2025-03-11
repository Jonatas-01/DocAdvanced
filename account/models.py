from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class PatientDetails(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    contact_info = models.EmailField(max_length=150)

    class Meta:
        verbose_name = "Patient Detail"
        verbose_name_plural = "Patient Details"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender})"
