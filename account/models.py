from django.db import models
from django.contrib.auth import get_user_model


class PatientDetails(models.Model):
    """
    Model class representing patient's detailed information.
    Attributes:
        user (User): One-to-one relationship with the User model
        first_name (str): Patient's first name
        last_name (str): Patient's last name
        age (int): Patient's age as a positive integer
        gender (str): Patient's gender, choice between 'Male' or 'Female'
        contact_info (str): Patient's email address
        medical_history (str): Optional text field for patient's medical history
        allergies (str): Optional text field for patient's allergies
    """
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
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Patient Detail"
        verbose_name_plural = "Patient Details"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender})"


class DoctorDetails(models.Model):
    """
    Model representing detailed information about a doctor.
    Attributes:
        user (User): One-to-one relationship with the base User model
        first_name (str): Doctor's first name
        last_name (str): Doctor's last name
        gender (str): Doctor's gender, chosen from GENDER_CHOICES
        contact_info (str): Doctor's contact email address
        specialty (str): Doctor's medical specialty, chosen from SPECIALTY_CHOICES
        about (text): Detailed description or biography of the doctor
    Constants:
        SPECIALTY_CHOICES (tuple): Available medical specialties
        GENDER_CHOICES (tuple): Available gender options
    """

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
