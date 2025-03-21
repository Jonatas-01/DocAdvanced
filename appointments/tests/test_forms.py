from django.test import TestCase
from appointments.forms import AppointmentRequestForm


class TestAppointmentRequestForm(TestCase):
    def setUp(self):
        """Set up data for tests"""
        self.form_data = {
            'notes': 'Test appointment notes'
        }

    def test_form_valid_data(self):
        """Test form with valid data"""
        form = AppointmentRequestForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        """Test form with empty data (should be valid as notes is not required)."""
        form = AppointmentRequestForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_notes_field_widget_attrs(self):
        """Test the widget attributes of the notes field."""
        form = AppointmentRequestForm()
        widget_attrs = form.fields['notes'].widget.attrs
        
        self.assertEqual(widget_attrs['class'], 'form-control')
        self.assertEqual(
            widget_attrs['placeholder'], 
            'Enter any additional information. E.g: feeling, urgent'
        )
        self.assertEqual(widget_attrs['rows'], 3)
    
    def test_form_meta_fields(self):
        """Test the Meta class fields attribute."""
        form = AppointmentRequestForm()
        self.assertEqual(form.Meta.fields, ('notes',))