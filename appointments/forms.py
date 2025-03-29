from django import forms
from .models import Appointment


class AppointmentRequestForm(forms.ModelForm):
    """
    A form class for handling appointment requests.
    This form is used to create or update appointment records, specifically focusing
    on capturing additional notes from the user. It is based on the Appointment model
    and only exposes the 'notes' field for user input.
    """

    class Meta:
        model = Appointment
        fields = ('notes',)

    notes = forms.CharField(
        widget=forms.Textarea(attrs={
                              'class': 'form-control', 'placeholder': 'Enter any additional information. E.g: feeling, urgent', 'rows': 3}),
        required=False
    )
