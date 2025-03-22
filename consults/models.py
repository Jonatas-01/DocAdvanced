from django.db import models
from appointments.models import PatientDetails, DoctorDetails

class Consult(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, related_name='consults_patient')
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.SET_NULL, null=True, related_name='consults_doctor')
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
        return f"Consult for {self.patient.first_name} by Dr. {self.doctor.first_name} on {self.created_at.strftime('%d-%m-%Y')}"
