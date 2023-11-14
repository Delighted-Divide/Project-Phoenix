from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name', 'email','address', 'phone_number', 'gender', 'birthday', 'city', 'country','nationality','language','hobby','marital_status', 'image']
    
