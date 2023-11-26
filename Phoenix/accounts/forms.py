from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name', 'email','address', 'phone_number', 'gender', 'birthday', 'city', 'country','nationality','language','hobby','marital_status', 'image']
    


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))