from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from .forms import DoctorForm
from accounts.forms import CustomUserForm
from accounts.models import CustomUser
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
# Create your views here.


def dashboard(request):

    context = {
        'pname': "Dashboard",
        'user': request.user
    }
    return render(request, "dashboard.html", context)


def doctor(request):
    doctor_list = Doctor.objects.all()  # Fetch all doctor objects
    paginator = Paginator(doctor_list, 7)  # 7 doctors per page
    page = request.GET.get('page')  # Get the page number from the query string
    doctors = paginator.get_page(page)  # Get the doctors for the current page
    context = {
        'pname': "Doctor",
        'user': request.user,
        'times': [i for i in range(7)],
        'doctors': doctors
    }
    return render(request, "doctor.html", context)



def doctor_profile(request,user_id  ):
    profile = CustomUser.objects.get(id=user_id)
    user_json = serializers.serialize('json', [profile])
    print(user_json)
    context = {
        'pname': "Profile",
        'user': request.user,
        'profile' : profile,
        'profile_json': user_json
    }
    return render(request, "doctor_profile.html", context)


def register(request):
    
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST,request.FILES, prefix='user')
        doctor_form = DoctorForm(request.POST, prefix='doctor')
        if user_form.is_valid() and doctor_form.is_valid():
            print('helo')
            user = user_form.save(commit=False)
            default_password = 'testpassword'  # Choose a strong default password
            user.password = make_password(default_password)
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user  # Assuming a one-to-one relationship
            doctor.save()
            doctor_form.save_m2m()
            return redirect('Dashboard')
    else:
        user_form = CustomUserForm(prefix='user')
        doctor_form = DoctorForm(prefix='doctor')
        print(doctor_form)

    context = {'pname':"Doctor User Creation",'user_form': user_form, 'doctor_form': doctor_form}
    return render(request, 'user.html', context)


