from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.messages import get_messages
from account.models import PatientDetails, DoctorDetails
from appointments.models import Appointment
from consults.models import Consult

User = get_user_model()


class ConsultViewsTest(TestCase):
    """Test suite for consult views."""

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

        # Create two appointments - one for existing consult, one for new consult test
        self.appointment_with_consult = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            status='confirmed',
            notes='Test appointment with consult'
        )

        self.appointment_without_consult = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            status='confirmed',
            notes='Test appointment without consult'
        )

        # Create consult for the first appointment
        self.consult = Consult.objects.create(
            appointment=self.appointment_with_consult,
            symptoms='Test symptoms',
            diagnosis='Test diagnosis',
            prescription='Test prescription'
        )

        # URLs
        self.consults_url = reverse('consults')
        self.start_consult_url = reverse(
            'start-consult', args=[self.appointment_without_consult.id])
        self.edit_consult_url = reverse('edit-consult', args=[self.consult.id])

    def test_consults_view_patient(self):
        """Test consults list view for patients."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(self.consults_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consults/consults_view.html')
        self.assertIn('consults', response.context)

    def test_consults_view_doctor(self):
        """Test consults list view for doctors."""
        self.client.login(username='testdoctor', password='testpass123')
        response = self.client.get(self.consults_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consults/consults_view.html')
        self.assertIn('consults', response.context)

    def test_start_consult_unauthorized(self):
        """Test unauthorized access to start consult view."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(self.start_consult_url)
        messages = list(get_messages(response.wsgi_request))

        self.assertRedirects(response, self.consults_url)
        self.assertIn('Only doctor has access to this page', str(messages[0]))

    def test_start_consult_get(self):
        """Test GET request to start consult view."""
        self.client.login(username='testdoctor', password='testpass123')
        response = self.client.get(self.start_consult_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consults/start_consult.html')
        self.assertIn('appointment', response.context)

    def test_start_consult_post_success(self):
        """Test successful consult creation."""
        self.client.login(username='testdoctor', password='testpass123')
        data = {
            'symptoms': 'New symptoms',
            'diagnosis': 'New diagnosis',
            'prescription': 'New prescription',
            'notes': 'Test notes'
        }
        response = self.client.post(self.start_consult_url, data)

        # Verify redirect
        self.assertRedirects(response, self.consults_url)

        # Verify consult was created
        new_consult = Consult.objects.get(appointment=self.appointment_without_consult)
        self.assertEqual(new_consult.symptoms, 'New symptoms')
        self.assertEqual(new_consult.diagnosis, 'New diagnosis')
        self.assertEqual(new_consult.prescription, 'New prescription')

        # Verify success message
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Consult has been created', str(messages[0]))

    def test_edit_consult_unauthorized(self):
        """Test unauthorized access to edit consult view."""
        self.client.login(username='testpatient', password='testpass123')
        response = self.client.get(self.edit_consult_url)

        self.assertRedirects(response, self.consults_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Only doctor has access to this page', str(messages[0]))

    def test_edit_consult_get(self):
        """Test GET request to edit consult view."""
        self.client.login(username='testdoctor', password='testpass123')
        response = self.client.get(self.edit_consult_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consults/edit_consult.html')
        self.assertIn('consult', response.context)

    def test_edit_consult_post_success(self):
        """Test successful consult update."""
        self.client.login(username='testdoctor', password='testpass123')
        data = {
            'symptoms': 'Updated symptoms',
            'diagnosis': 'Updated diagnosis',
            'prescription': 'Updated prescription',
            'notes': 'Updated notes'
        }
        response = self.client.post(self.edit_consult_url, data)

        self.assertRedirects(response, self.consults_url)
        self.consult.refresh_from_db()
        self.assertEqual(self.consult.symptoms, 'Updated symptoms')
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Consult updated successfully', str(messages[0]))

    def test_delete_consult(self):
        """Test consult deletion."""
        self.client.login(username='testdoctor', password='testpass123')
        data = {'consult_id': self.consult.id}
        response = self.client.post(self.consults_url, data)

        self.assertRedirects(response, self.consults_url)
        self.assertFalse(Consult.objects.filter(id=self.consult.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Your consult has been deleted', str(messages[0]))
