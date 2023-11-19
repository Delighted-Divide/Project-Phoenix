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
from django.utils import timezone
# Create your views here.




def page_sort(pagination):
        pages = pagination.paginator.num_pages
        current = pagination.number 
        if 1 <= current <= 15:
            return (1,16)
        elif pages-16 <= current <= pages:
            return (pages-17,pages)
        else:
            return(current-8,current+8)
        

def dashboard(request):
    patient_count = Patient.objects.all().count()
    doctor_count = Doctor.objects.all().count()
    visitors = InpatientVisit.objects.all().count() + OutpatientVisit.objects.all().count()
    bed_occupied = Bed.objects.all().filter(is_occupied=True).count()
    bed_occupancy = int(bed_occupied/Bed.objects.all().count())
    context = {
        'pname': "Dashboard",
        'user': request.user,
        'patient':patient_count,
        'doctor':doctor_count,
        'bed':bed_occupancy,
        'visitors':visitors
    }
    return render(request, "dashboard.html", context)


def doctor(request):
    doctor_list = Doctor.objects.all()  # Fetch all doctor objects
    paginator = Paginator(doctor_list, 7)  # 7 doctors per page
    page = request.GET.get('page')  # Get the page number from the query string
    doctors = paginator.get_page(page)  # Get the doctors for the current page

    start,end = page_sort(doctors)
    context = {
        'pname': "Doctor",
        'user': request.user,
        'doctors': doctors,
        'start_page':start,
        'end_page':end
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
        'profile_json': user_json,
        
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


 
        
    start,end = page_sort(patients)
    print(start,end)
    current_page = int(page_number) if page_number else 1
    start_index = (current_page - 1) * paginator.per_page
    context = {
        'pname': "Patient",
        'user': request.user,
        'patients': patients,
        'start_index': start_index,
        'start_page':start,
        'end_page':end
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

        
    start,end = page_sort(rooms)

    context = {
        'pname': "Room",
        'user': request.user,
        'rooms': rooms,
        'start_page':start,
        'end_page':end
    }
    return render(request, "room.html", context)




def surgery(request):
    surgery_list = Surgery.objects.all()
    now = timezone.now()
    past_surgeries = Surgery.objects.filter(scheduled_time__lt=now)
    future_surgeries = Surgery.objects.filter(scheduled_time__gt=now)
    current_surgeries = Surgery.objects.filter(scheduled_time=now)

    # room_type = request.GET.get('roomType')
    # search_query = request.GET.get('searchQuery')

    # if room_type:
    #     room_list = room_list.filter(room_type=room_type)

    # if search_query:
    #     room_list = room_list.filter(
    #         Q(room_id__icontains=search_query) 
    #         # Add more fields to search within as per your model
    #     )

    def pagination(surgery_list):
        paginator = Paginator(surgery_list,12)  
        page_number = request.GET.get('page')  
        surgeries = paginator.get_page(page_number)  
        return surgeries
    
    past_surgeries = pagination(past_surgeries)
    future_surgeries = pagination(future_surgeries)

    start_past_surgeries , end_past_surgeries = page_sort(past_surgeries)

    context = {
        'pname': "Surgery",
        'user': request.user,
        'past_surgeries': past_surgeries,
        'future_surgeries' : future_surgeries,
        'start_past_surgeries': start_past_surgeries,
        'end_past_surgeries' : end_past_surgeries
    }
    return render(request, "surgery.html", context)




def appointment(request):
    appointment_list = Appointment.objects.all()  # Fetch all doctor objects
    paginator = Paginator(appointment_list, 20)  # 7 doctors per page
    page = request.GET.get('page')  # Get the page number from the query string
    appointments = paginator.get_page(page)  # Get the doctors for the current page

    start,end = page_sort(appointments)
    context = {
        'pname': "Appointment",
        'user': request.user,
        'doctors': appointments,
        'start_page':start,
        'end_page':end
    }
    return render(request, "appointment.html", context)
