from .models import CustomUser
from rest_framework import viewsets
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
# Create your views here.


def log(request, uname):
    user = CustomUser.objects.get(username=uname)
    login(request, user)
    return redirect('/')


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/room/')  # Redirect to a success page.
            else:
                # Handle the case where authentication fails
                form.add_error(None, "Invalid username or password")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})