from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from account.models import PatientDetails, DoctorDetails

User = get_user_model()


class TestAccountViews(TestCase):
    """Extended test suite for views in the account app."""

    def setUp(self):
        self.client = Client()

        self.patient_user = User.objects.create_user(
            username='patient1', password='pass', role='patient')
        self.doctor_user = User.objects.create_user(
            username='doctor1', password='pass', role='doctor')
        self.account_details_url = reverse('account-details')
        self.edit_details_url = reverse('edit-details')
        self.patient_form_url = reverse('patient-form')
        self.doctor_form_url = reverse('doctor-form')

    #  PATIENT VIEWS
    def test_patient_redirects_to_form_if_no_details(self):
        """
        If patient has no patient details, they should be redirected to 'patient-form'.
        """
        self.client.login(username='patient1', password='pass')
        response = self.client.get(self.account_details_url)
        self.assertRedirects(response, self.patient_form_url)

    def test_patient_can_access_account_if_details_exist(self):
        """
        If the patient has details, they can access 'account-details'.
        """
        self.client.login(username='patient1', password='pass')
        PatientDetails.objects.create(
            user=self.patient_user,
            first_name='Test',
            last_name='Patient',
            age=30,
            gender='Female',
            contact_info='test@example.com'
        )
        response = self.client.get(self.account_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/patient_details.html')

    def test_patient_form_submission(self):
        """
        POSTing valid data to 'patient_form' should create patient details and redirect.
        """
        self.client.login(username='patient1', password='pass')
        data = {
            'first_name': 'Mary',
            'last_name': 'Patient',
            'age': 25,
            'gender': 'Female',
            'contact_info': 'marypatient@example.com'
        }
        response = self.client.post(self.patient_form_url, data)
        self.assertEqual(response.status_code, 302)
        exists = PatientDetails.objects.filter(user=self.patient_user).exists()
        self.assertTrue(exists)

    #  DOCTOR VIEWS
    def test_doctor_redirects_to_form_if_no_details(self):
        """
        If doctor has no doctor details, they should be redirected to 'doctor-form'.
        """
        self.client.login(username='doctor1', password='pass')
        response = self.client.get(self.account_details_url)
        self.assertRedirects(response, self.doctor_form_url)

    def test_doctor_can_access_account_if_details_exist(self):
        """
        If the doctor has details, they can access 'account-details'.
        """
        self.client.login(username='doctor1', password='pass')
        DoctorDetails.objects.create(
            user=self.doctor_user,
            first_name='Dr.',
            last_name='Who',
            gender='Male',
            contact_info='doctor@example.com',
            specialty='Neurology',
            about='Expert in neurology.'
        )
        response = self.client.get(self.account_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/doctor_details.html')

    def test_doctor_form_submission(self):
        """
        POSTing valid data to 'doctor_form' should create doctor details and redirect.
        """
        self.client.login(username='doctor1', password='pass')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'gender': 'Male',
            'contact_info': 'doc@example.com',
            'specialty': 'Cardiology',
            'about': 'Expert in heart surgery.'
        }
        response = self.client.post(self.doctor_form_url, data)
        self.assertEqual(response.status_code, 302)
        exists = DoctorDetails.objects.filter(user=self.doctor_user).exists()
        self.assertTrue(exists)

    #  EDIT DETAILS
    def test_edit_details_for_patient(self):
        """
        Test editing patient details with valid data.
        """
        self.client.login(username='patient1', password='pass')
        pd = PatientDetails.objects.create(
            user=self.patient_user,
            first_name='Old',
            last_name='Name',
            age=40,
            gender='Female',
            contact_info='old@example.com'
        )

        response = self.client.post(self.edit_details_url, {
            'first_name': 'New',
            'last_name': 'Patient',
            'age': 22,
            'gender': 'Female',
            'contact_info': 'new@example.com',
        })
        self.assertRedirects(response, self.account_details_url)

        pd.refresh_from_db()
        self.assertEqual(pd.first_name, 'New')
        self.assertEqual(pd.contact_info, 'new@example.com')

    def test_edit_details_for_doctor(self):
        """
        Test editing doctor details with valid data.
        """
        self.client.login(username='doctor1', password='pass')
        dd = DoctorDetails.objects.create(
            user=self.doctor_user,
            first_name='Dr.',
            last_name='Strange',
            gender='Male',
            contact_info='strange@example.com',
            specialty='Neurology',
            about='Old about.'
        )

        response = self.client.post(self.edit_details_url, {
            'first_name': 'Dr. New',
            'last_name': 'Name',
            'gender': 'Male',
            'contact_info': 'newdoc@example.com',
            'specialty': 'Orthopedics',
            'about': 'New about me.'
        })
        self.assertRedirects(response, self.account_details_url)

        dd.refresh_from_db()
        self.assertEqual(dd.first_name, 'Dr. New')
        self.assertEqual(dd.specialty, 'Orthopedics')
