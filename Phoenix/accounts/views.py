from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from .models import CustomUser

# Create your views here.


def log(request, uname):
    user = CustomUser.objects.get(username=uname)
    login(request, user)
    return redirect('/')
