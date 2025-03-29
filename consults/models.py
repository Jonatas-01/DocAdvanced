from django.db import models
from appointments.models import Appointment


class Consult(models.Model):
    """
    A Django model representing a medical consultation record.
    This model stores detailed information about a medical consultation, including patient
    symptoms, medical history, and the doctor's diagnosis and prescription.
    """

    appointment = models.OneToOneField(
        Appointment, on_delete=models.CASCADE, related_name='consult')

    # Intake section
    symptoms = models.TextField()
    allergies = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    # Consultation result
    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consult for {self.appointment.patient.first_name} by Dr. {self.appointment.doctor.first_name} on {self.created_at.strftime('%d-%m-%Y')}"
