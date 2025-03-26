from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from account.models import PatientDetails, DoctorDetails

User = get_user_model()


class PatientDetailsModelTest(TestCase):
    """Test suite for the PatientDetails model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='patient'
        )
        self.patient_data = {
            'user': self.user,
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
            'gender': 'Male',
            'contact_info': 'john.doe@example.com'
        }

    def test_create_patient_details(self):
        """Test creating a patient details instance"""
        patient = PatientDetails.objects.create(**self.patient_data)
        self.assertEqual(patient.first_name, 'John')
        self.assertEqual(patient.last_name, 'Doe')
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, 'Male')
        self.assertEqual(patient.contact_info, 'john.doe@example.com')

    def test_patient_gender_choices(self):
        """Test gender choices validation"""
        invalid_data = self.patient_data.copy()
        invalid_data['gender'] = 'Invali' # cut one letter because gender only acceppt max 6 letters
        with self.assertRaises(ValidationError):
            patient = PatientDetails.objects.create(**invalid_data)
            patient.full_clean()

    def test_patient_email_validation(self):
        """Test email validation"""
        invalid_data = self.patient_data.copy()
        invalid_data['contact_info'] = 'invalid-email'
        with self.assertRaises(ValidationError):
            patient = PatientDetails.objects.create(**invalid_data)
            patient.full_clean()


class DoctorDetailsModelTest(TestCase):
    """Test suite for the DoctorDetails model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testdoctor',
            password='testpass123',
            role='doctor'
        )
        self.doctor_data = {
            'user': self.user,
            'first_name': 'Dr',
            'last_name': 'Smith',
            'gender': 'Male',
            'contact_info': 'dr.smith@example.com',
            'specialty': 'Cardiology',
            'about': 'Experienced cardiologist'
        }

    def test_create_doctor_details(self):
        """Test creating a doctor details instance"""
        doctor = DoctorDetails.objects.create(**self.doctor_data)
        self.assertEqual(doctor.first_name, 'Dr')
        self.assertEqual(doctor.last_name, 'Smith')
        self.assertEqual(doctor.specialty, 'Cardiology')
        self.assertEqual(doctor.contact_info, 'dr.smith@example.com')
    
    def test_specialty_choices(self):
        """Test specialty choices validation"""
        invalid_data = self.doctor_data.copy()
        invalid_data['specialty'] = 'InvalidSpecialty'
        with self.assertRaises(ValidationError):
            doctor = DoctorDetails.objects.create(**invalid_data)
            doctor.full_clean()

    def test_gender_choices(self):
        """Test gender choices validation"""
        invalid_data = self.doctor_data.copy()
        invalid_data['gender'] = 'Invali' # cut one letter because gender only acceppt max 6 letters
        with self.assertRaises(ValidationError):
            doctor = DoctorDetails.objects.create(**invalid_data)
            doctor.full_clean()

    def test_email_validation(self):
        """Test email validation"""
        invalid_data = self.doctor_data.copy()
        invalid_data['contact_info'] = 'invalid-email'
        with self.assertRaises(ValidationError):
            doctor = DoctorDetails.objects.create(**invalid_data)
            doctor.full_clean()
    
    def test_unique_user_constraint(self):
        """Test that a user can only have one doctor details record"""
        DoctorDetails.objects.create(**self.doctor_data)
        duplicate_data = self.doctor_data.copy()
        with self.assertRaises(Exception):
            DoctorDetails.objects.create(**duplicate_data)
