from django.test import TestCase
from core.forms import ProfileCreationForm
from core.models import Profile


class TestProfileCreationForm(TestCase):
    """Test suite for the ProfileCreationForm."""

    def setUp(self):
        """Set up test data."""
        self.form_data = {
            'username': 'testuser',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'role': 'patient'
        }

    def test_form_valid_data(self):
        """Test form with valid data."""
        form = ProfileCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_password_mismatch(self):
        """Test form with mismatched passwords."""
        self.form_data['password2'] = 'DifferentPass123!'
        form = ProfileCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_form_invalid_role(self):
        """Test form with invalid role."""
        self.form_data['role'] = 'invalid_role'
        form = ProfileCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('role', form.errors)

    def test_form_missing_required_fields(self):
        """Test form with missing required fields."""
        form = ProfileCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)
        self.assertIn('role', form.errors)
