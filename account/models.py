from django.db import models
from django.contrib.auth import get_user_model


class PatientDetails(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
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


class DoctorDetails(models.Model):
    SPECIALTY_CHOICES = (
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Neurology', 'Neurology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Otolaryngology', 'Otolaryngology'),
        ('Dermatology', 'Dermatology'),
        ('Gynecology', 'Gynecology'),
        ('Urology', 'Urology'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    contact_info = models.EmailField(max_length=150)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)
    about = models.TextField()

    class Meta:
        verbose_name = "Doctor Detail"
        verbose_name_plural = "Doctor Details"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialty})"
