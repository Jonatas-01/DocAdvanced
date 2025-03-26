from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Profile


class TestProfileModel(TestCase):
    """Test suite for the Profile model."""

    def setUp(self):
        """Set up test data."""
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'role': 'patient'
        }
        self.user = Profile.objects.create_user(**self.user_data)

    def test_create_user(self):
        """Test creating a new user."""
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.role, self.user_data['role'])
        self.assertTrue(self.user.check_password(self.user_data['password']))
    
    def test_create_doctor_user(self):
        """Test creating a user with doctor role."""
        doctor = Profile.objects.create_user(
            username='doctor',
            email='doctor@example.com',
            password='testpass123',
            role='doctor'
        )
        self.assertEqual(doctor.role, 'doctor')

    def test_role_choices(self):
        """Test the role choices are correctly defined."""
        expected_choices = (('patient', 'Patient'), ('doctor', 'Doctor'))
        self.assertEqual(Profile.ROLE_CHOICES, expected_choices)
