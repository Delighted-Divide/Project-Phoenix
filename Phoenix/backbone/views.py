from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from .forms import DoctorForm
from accounts.forms import CustomUserForm
from accounts.models import CustomUser
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.db.models import Q
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


    context = {'pname':"Doctor User Creation",'user_form': user_form, 'doctor_form': doctor_form}
    return render(request, 'user.html', context)

def patient(request):
    patient_list = Patient.objects.all()
    paginator = Paginator(patient_list,12)  
    page_number = request.GET.get('page')  
    patients = paginator.get_page(page_number)  


    current_page = int(page_number) if page_number else 1
    start_index = (current_page - 1) * paginator.per_page
    context = {
        'pname': "Patient",
        'user': request.user,
        'patients': patients,
        'start_index': start_index
    }
    return render(request, "patient.html", context)


def room(request):
    room_list = Room.objects.all()

    room_type = request.GET.get('roomType')
    search_query = request.GET.get('searchQuery')

    if room_type:
        room_list = room_list.filter(room_type=room_type)

    if search_query:
        room_list = room_list.filter(
            Q(room_id__icontains=search_query) 
            # Add more fields to search within as per your model
        )
    paginator = Paginator(room_list,14)  
    page_number = request.GET.get('page')  
    rooms = paginator.get_page(page_number)  


    context = {
        'pname': "Room",
        'user': request.user,
        'rooms': rooms,
    }
    return render(request, "room.html", context)