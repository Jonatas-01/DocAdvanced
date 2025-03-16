from django import forms
from .models import Appointment

class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('notes',)

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any additional information. E.g: feeling, urgent', 'rows': 3}),
        required=False
    )