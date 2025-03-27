from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from account.models import PatientDetails, DoctorDetails
from appointments.models import Appointment
from consults.models import Consult

User = get_user_model()


class ConsultModelTest(TestCase):
    """Test suite for the Consult model."""

    def setUp(self):
        """Set up test data."""
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

        # Create details
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

        # Create appointment
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            status='confirmed',
            notes='Test appointment'
        )

        # Basic consult data
        self.consult_data = {
            'appointment': self.appointment,
            'symptoms': 'Test symptoms',
            'diagnosis': 'Test diagnosis',
            'prescription': 'Test prescription'
        }

    def test_create_basic_consult(self):
        """Test creating a basic consult with required fields."""
        consult = Consult.objects.create(**self.consult_data)
        self.assertEqual(consult.symptoms, 'Test symptoms')
        self.assertEqual(consult.diagnosis, 'Test diagnosis')
        self.assertEqual(consult.prescription, 'Test prescription')
        self.assertIsNone(consult.notes)
        self.assertIsNotNone(consult.created_at)

    def test_consult_string_representation(self):
        """Test the string representation of a consult."""
        consult = Consult.objects.create(**self.consult_data)
        expected_str = f"Consult for Test by Dr. Test on {consult.created_at.strftime('%d-%m-%Y')}"
        self.assertEqual(str(consult), expected_str)

    def test_consult_optional_fields(self):
        """Test consult creation with optional fields."""
        data = self.consult_data.copy()
        data.update({
            'allergies': 'Test allergies',
            'medications': 'Test medications',
            'notes': 'Test notes'
        })
        consult = Consult.objects.create(**data)
        self.assertEqual(consult.allergies, 'Test allergies')
        self.assertEqual(consult.medications, 'Test medications')
        self.assertEqual(consult.notes, 'Test notes')

    def test_consult_required_fields(self):
        """Test that required fields raise validation error when missing."""
        required_fields = ['symptoms', 'diagnosis', 'prescription']

        for field in required_fields:
            data = self.consult_data.copy()
            data[field] = ''

            consult = Consult(**data)

            with self.assertRaises(ValidationError):
                consult.full_clean()

    def test_consult_appointment_relationship(self):
        """Test the OneToOne relationship with appointment."""
        consult = Consult.objects.create(**self.consult_data)
        self.assertEqual(consult.appointment, self.appointment)
        self.assertEqual(self.appointment.consult, consult)

    def test_consult_cascade_delete(self):
        """Test that consult is deleted when appointment is deleted."""
        consult = Consult.objects.create(**self.consult_data)
        consult_id = consult.id
        self.appointment.delete()
        self.assertFalse(Consult.objects.filter(id=consult_id).exists())

    def test_consult_timestamps(self):
        """Test that created_at is automatically set."""
        before = timezone.now()
        consult = Consult.objects.create(**self.consult_data)
        after = timezone.now()
        self.assertTrue(before <= consult.created_at <= after)

    def test_consult_unique_appointment(self):
        """Test that one appointment can only have one consult."""
        Consult.objects.create(**self.consult_data)

        with self.assertRaises(Exception):
            Consult.objects.create(**self.consult_data)

