from django.test import TestCase
from account.forms import PatientlDetailsForm, DoctorDetailsForm
from account.models import PatientDetails, DoctorDetails


class TestPatientForm(TestCase):
    """Test cases for the PatientDetailsForm"""

    def setUp(self):
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
            'gender': 'Male',
            'contact_info': 'john.doe@example.com'
        }

    def test_patient_form_valid_data(self):
        """Test form is valid with correct data"""
        form = PatientlDetailsForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_patient_form_no_data(self):
        """Test form is invalid with no data"""
        form = PatientlDetailsForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_patient_form_invalid_age(self):
        """Test form validation with invalid age"""
        invalid_data = self.valid_data.copy()
        invalid_data['age'] = -1
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)

    def test_patient_form_invalid_email(self):
        """Test form validation with invalid email"""
        invalid_data = self.valid_data.copy()
        invalid_data['contact_info'] = 'not-an-email'
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_info', form.errors)

    def test_patient_form_invalid_gender(self):
        """Test form validation with invalid gender choice"""
        invalid_data = self.valid_data.copy()
        invalid_data['gender'] = 'Invalid'
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('gender', form.errors)


class TestDoctorForm(TestCase):
    """Test cases for the DoctorDetailsForm"""

    def setUp(self):
        self.valid_data = {
            'first_name': 'Dr.',
            'last_name': 'Smith',
            'gender': 'Male',
            'contact_info': 'dr.smith@hospital.com',
            'specialty': 'Cardiology',
            'about': 'Experienced cardiologist with 10 years of practice.'
        }

    def test_doctor_form_valid_data(self):
        """Test form is valid with correct data"""
        form = DoctorDetailsForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
    
    def test_patient_form_no_data(self):
        """Test form is invalid with no data"""
        form = PatientlDetailsForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_patient_form_invalid_age(self):
        """Test form validation with invalid age"""
        invalid_data = self.valid_data.copy()
        invalid_data['age'] = -1
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)

    def test_patient_form_invalid_email(self):
        """Test form validation with invalid email"""
        invalid_data = self.valid_data.copy()
        invalid_data['contact_info'] = 'not-an-email'
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_info', form.errors)

    def test_patient_form_invalid_gender(self):
        """Test form validation with invalid gender choice"""
        invalid_data = self.valid_data.copy()
        invalid_data['gender'] = 'Invalid'
        form = PatientlDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('gender', form.errors)


class TestDoctorForm(TestCase):
    """Test cases for the DoctorDetailsForm"""

    def setUp(self):
        self.valid_data = {
            'first_name': 'Dr.',
            'last_name': 'Smith',
            'gender': 'Male',
            'contact_info': 'dr.smith@hospital.com',
            'specialty': 'Cardiology',
            'about': 'Experienced cardiologist with 10 years of practice.'
        }

    def test_doctor_form_valid_data(self):
        """Test form is valid with correct data"""
        form = DoctorDetailsForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_doctor_form_no_data(self):
        """Test form is invalid with no data"""
        form = DoctorDetailsForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_doctor_form_invalid_specialty(self):
        """Test form validation with invalid specialty"""
        invalid_data = self.valid_data.copy()
        invalid_data['specialty'] = 'NotASpecialty'
        form = DoctorDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('specialty', form.errors)

    def test_doctor_form_invalid_email(self):
        """Test form validation with invalid email"""
        invalid_data = self.valid_data.copy()
        invalid_data['contact_info'] = 'not-an-email'
        form = DoctorDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_info', form.errors)

    def test_doctor_form_empty_about(self):
        """Test form validation with empty about field"""
        invalid_data = self.valid_data.copy()
        invalid_data['about'] = ''
        form = DoctorDetailsForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('about', form.errors)
