from django.db import models
from account.models import DoctorDetails, PatientDetails


class Appointment(models.Model):
    """
    Represents a medical appointment between a patient and a doctor.
    This model stores all the necessary information about medical appointments,
    including the status, scheduling details, and any additional notes.
    """

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled'),
    ]

    patient = models.ForeignKey(
        PatientDetails, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(
        DoctorDetails, on_delete=models.CASCADE, related_name='appointments_received')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    requested_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    # doctor fill when accepted
    scheduled_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.first_name} by {self.patient.first_name} - {self.get_status_display()}"
