from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from account.models import PatientDetails, DoctorDetails
from appointments.models import Appointment

User = get_user_model()


class AppointmentViewsTest(TestCase):
    """Test suite for appointment views."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()

        # Create users
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

        # Create user details
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

        # Create test appointment
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            notes='Test appointment',
            status='pending'
        )

        # URLs
        self.appointments_url = reverse('appointments')
        self.request_appointment_url = reverse(
            'request_appointment', args=[self.doctor.id])

    def test_appointments_view_patient(self):
        """Test appointments view for patients."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(self.appointments_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient/appointments_patient_view.html')
        self.assertIn('pending_appointments', response.context)
        self.assertIn('confirmed_appointments', response.context)
        self.assertIn('doctors', response.context)

    def test_appointments_view_doctor(self):
        """Test appointments view for doctors."""
        self.client.login(username='testdoctor', password='testpass123')
        response = self.client.get(self.appointments_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor/appointment_doctor_view.html')
        self.assertIn('pending_appointments', response.context)
        self.assertIn('confirmed_appointments', response.context)
    
    def test_request_appointment_view(self):
        """Test appointment request view."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(self.request_appointment_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form/request_appointment.html')
    
    def test_appointment_actions_doctor(self):
        """Test doctor appointment actions."""
        self.client.login(username='testdoctor', password='testpass123')
        
        # Test confirm appointment
        response = self.client.post(self.appointments_url, {
            'appointment_id': self.appointment.id,
            'action': 'confirm',
            'scheduled_date': timezone.now()
        })
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, 'confirmed')

        # Test reject appointment
        response = self.client.post(self.appointments_url, {
            'appointment_id': self.appointment.id,
            'action': 'reject'
        })
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, 'rejected')
    
    def test_appointment_actions_patient(self):
        """Test patient appointment actions."""
        self.client.login(username='testpatient', password='testpass123')
        
        # Test cancel appointment
        response = self.client.post(self.appointments_url, {
            'appointment_id': self.appointment.id,
            'action': 'cancel'
        })
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, 'canceled')

        # Test edit appointment notes
        new_notes = 'Updated test notes'
        response = self.client.post(self.appointments_url, {
            'appointment_id': self.appointment.id,
            'action': 'edit',
            'notes': new_notes
        })
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.notes, new_notes)
    
    def test_unauthorized_access(self):
        """Test unauthorized access attempts."""
        # Test patient accessing doctor view
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(reverse('appointments'))
        self.assertNotEqual(response.status_code, 403)

        # Test doctor accessing patient request view
        self.client.login(username='testdoctor', password='testpass123')
        response = self.client.get(self.request_appointment_url)
        self.assertEqual(response.status_code, 302)
    
    def test_appointment_creation(self):
        """Test appointment creation through request view."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.post(self.request_appointment_url, {
            'notes': 'New appointment request'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Appointment.objects.filter(
                patient=self.patient, 
                doctor=self.doctor,
                notes='New appointment request'
            ).exists()
        )