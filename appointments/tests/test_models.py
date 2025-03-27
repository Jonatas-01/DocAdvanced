from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from account.models import PatientDetails, DoctorDetails
from appointments.models import Appointment

User = get_user_model()


class AppointmentModelTest(TestCase):
    """Test suite for the Appointment model."""

    def setUp(self):
        """Set up test data."""
        # Create test users
        self.patient_user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='patient'
        )
        self.doctor_user = User.objects.create_user(
            username='testdoctor',
            password='testpass123',
            role='doctor'
        )

        # Create patient and doctor details
        self.patient = PatientDetails.objects.create(
            user=self.patient_user,
            first_name='Test',
            last_name='Patient',
            age=25,
            gender='Male',
            contact_info='patient@test.com'
        )

        self.doctor = DoctorDetails.objects.create(
            user=self.doctor_user,
            first_name='Test',
            last_name='Doctor',
            gender='Male',
            contact_info='doctor@test.com',
            specialty='Cardiology',
            about='Test doctor bio'
        )

        # Create base appointment data
        self.appointment_data = {
            'patient': self.patient,
            'doctor': self.doctor,
            'notes': 'Test appointment notes',
            'status': 'pending'
        }

    def test_create_appointment(self):
        """Test creating a basic appointment."""
        appointment = Appointment.objects.create(**self.appointment_data)
        self.assertEqual(appointment.patient, self.patient)
        self.assertEqual(appointment.doctor, self.doctor)
        self.assertEqual(appointment.status, 'pending')
        self.assertEqual(appointment.notes, 'Test appointment notes')
        self.assertIsNotNone(appointment.requested_date)

    def test_appointment_status_choices(self):
        """Test that appointment status must be one of the defined choices."""
        appointment = Appointment.objects.create(**self.appointment_data)

        # Test valid status changes
        valid_statuses = ['pending', 'confirmed',
                          'rejected', 'closed', 'canceled']
        for status in valid_statuses:
            appointment.status = status
            appointment.save()
            self.assertEqual(appointment.status, status)

        # Test invalid status
        with self.assertRaises(ValidationError):
            appointment.status = 'invalid_status'
            appointment.full_clean()

    def test_appointment_scheduling(self):
        """Test scheduling an appointment with a date."""
        appointment = Appointment.objects.create(**self.appointment_data)
        scheduled_date = timezone.now()

        appointment.status = 'confirmed'
        appointment.scheduled_date = scheduled_date
        appointment.save()

        self.assertEqual(appointment.status, 'confirmed')
        self.assertEqual(appointment.scheduled_date, scheduled_date)

    def test_appointment_deletion_cascade(self):
        """Test that appointments are deleted when related patient/doctor is deleted."""
        appointment = Appointment.objects.create(**self.appointment_data)

        # Test patient deletion
        self.patient.delete()
        self.assertFalse(Appointment.objects.filter(
            id=appointment.id).exists())

        # Create new appointment for doctor deletion test
        new_patient = PatientDetails.objects.create(
            user=User.objects.create_user(
                username='newpatient',
                password='testpass123',
                role='patient'
            ),
            first_name='New',
            last_name='Patient',
            age=30,
            gender='Female',
            contact_info='newpatient@test.com'
        )

        new_appointment = Appointment.objects.create(
            patient=new_patient,
            doctor=self.doctor,
            notes='Test appointment notes',
            status='pending'
        )

        # Test doctor deletion
        self.doctor.delete()
        self.assertFalse(Appointment.objects.filter(
            id=new_appointment.id).exists())

    def test_appointment_notes_optional(self):
        """Test that appointment notes are optional."""
        appointment_data = self.appointment_data.copy()
        appointment_data.pop('notes')

        appointment = Appointment.objects.create(**appointment_data)
        self.assertIsNone(appointment.notes)

    def test_multiple_appointments_same_patient_doctor(self):
        """Test that a patient can have multiple appointments with the same doctor."""
        first_appointment = Appointment.objects.create(**self.appointment_data)
        second_appointment = Appointment.objects.create(
            **self.appointment_data)

        patient_appointments = Appointment.objects.filter(
            patient=self.patient,
            doctor=self.doctor
        )

        self.assertEqual(patient_appointments.count(), 2)
        self.assertNotEqual(first_appointment.requested_date,
                            second_appointment.requested_date)
