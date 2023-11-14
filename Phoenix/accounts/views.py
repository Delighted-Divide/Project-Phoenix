from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserForm
from backbone.forms import DoctorForm
# Create your views here.


def log(request, uname):
    user = CustomUser.objects.get(username=uname)
    login(request, user)
    return redirect('/')


