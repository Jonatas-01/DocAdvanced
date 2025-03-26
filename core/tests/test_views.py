from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from core.models import Profile
from core.forms import ProfileCreationForm


class TestViews(TestCase):
    """Test suite for core views."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        
        # Create test user
        self.user_data = {
            'username': 'testuser',
            'password': 'TestPass123!',
            'role': 'patient'
        }
        self.user = Profile.objects.create_user(**self.user_data)

    def test_home_view(self):
        """Test home page view."""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_registration_view_GET(self):
        """Test registration page GET request."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')
        self.assertIsInstance(response.context['form'], ProfileCreationForm)

    def test_registration_view_POST_valid(self):
        """Test registration with valid data."""
        data = {
            'username': 'newuser',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'role': 'patient'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(Profile.objects.count(), 2)
        self.assertRedirects(response, reverse('patient-form'))

    def test_registration_view_POST_invalid(self):
        """Test registration with invalid data."""
        data = {
            'username': '',
            'password1': 'test',
            'password2': 'test',
            'role': 'invalid'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_login_view_GET(self):
        """Test login page GET request."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_view_POST_valid(self):
        """Test login with valid credentials."""
        data = {
            'username': 'testuser',
            'password': 'TestPass123!'
        }
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, self.home_url)

    def test_login_view_POST_invalid(self):
        """Test login with invalid credentials."""
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid username or password')

    def test_logout_view_GET(self):
        """Test logout page GET request."""
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/logout.html')

    def test_logout_view_POST(self):
        """Test logout functionality."""
        self.client.login(username='testuser', password='TestPass123!')
        response = self.client.post(self.logout_url)
        self.assertRedirects(response, self.login_url)

    def test_authenticated_user_redirect(self):
        """Test redirects for authenticated users."""
        self.client.login(username='testuser', password='TestPass123!')
        
        # Test registration page redirect
        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url)
        
        # Test login page redirect
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.home_url)