from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['id', 'user']  # Assuming 'user' field contains the ID reference to CustomUser