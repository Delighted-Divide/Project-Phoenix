from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from .forms import DoctorForm
from accounts.forms import CustomUserForm
from accounts.models import CustomUser,Medicine
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
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
    bed_occupancy = int(bed_occupied/Bed.objects.all().count()*100)
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
    doctor_list = Doctor.objects.all()  
    paginator = Paginator(doctor_list, 7) 
    page = request.GET.get('page')  
    doctors = paginator.get_page(page) 

    start,end = page_sort(doctors)
    context = {
        'pname': "Doctor",
        'user': request.user,
        'doctors': doctors,
        'start_page':start,
        'end_page':end
    }
    return render(request, "doctor.html", context)



def doctor_profile(request,user_id):
    profile = CustomUser.objects.get(id=user_id)
    user_json = serializers.serialize('json', [profile])
    
  
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
    paginator = Paginator(patient_list,13)  
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
    start_future_surgeries , end_future_surgeries = page_sort(future_surgeries)

    context = {
        'pname': "Surgery",
        'user': request.user,
        'past_surgeries': past_surgeries,
        'future_surgeries' : future_surgeries,
        'start_past_surgeries': start_past_surgeries,
        'end_past_surgeries' : end_past_surgeries,
        'start_future_surgeries':start_future_surgeries,
        'end_future_surgeries':end_future_surgeries
    }
    return render(request, "surgery.html", context)




def appointment(request):
    today = datetime.now()
    appointment_list = Appointment.objects.filter(Q(doctor=request.user.doctor_profile) & Q(appointment_date__gte = today))  # Fetch all doctor objects
    
    hours = [
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23',
]
    days_of_week = []
    dates_of_week = []
    week = {}
    appointment_json = {}

    # Loop to get the next 7 days along with their day names

    for i in range(7):
        next_day = today + timedelta(days=i)
        day_name = next_day.strftime('%A')  # Getting the name of the day
        formatted_date = next_day.strftime('%d')
        days_of_week.append(day_name[:3])
        dates_of_week.append(formatted_date)
        week[formatted_date] = day_name[:3]


    for appointment in appointment_list:
        id_creation = appointment.appointment_date.strftime('%d') + "-" + str(appointment.start_time)
        appointment_json[id_creation] = appointment.patient.first_name




    context = {
        'pname': "Appointment",
        'user': request.user,

        'hours':hours,
        'days' : days_of_week,
        'dates':dates_of_week,
        'week':week,
        'json' : appointment_json
    }
    return render(request, "appointment.html", context)




def laboratory(request):

    context = {
        'pname': "Laboratory",
        'user': request.user,

    }
    return render(request, "laboratory.html", context)


def lab(request,lab_name):
    lab = Lab.objects.get(name= lab_name)
    test_list = LabTest.objects.filter(lab=lab) 
    scan_list = ScanTest.objects.filter(lab=lab)  


    context = {
        'pname': lab_name.title,
        'user': request.user,
        'tests':test_list,
        'scans':scan_list
        
        }
    return render(request, "labs.html", context)



def duty(request):
    today = timezone.localdate()
    days_ahead = [today + timedelta(days=i) for i in range(7)]
    weekdays = [day.strftime("%A") for day in days_ahead]

    shifts_by_day = {}
    for weekday in weekdays:
        shifts = DoctorWorkShift.objects.filter(
            doctor=request.user.doctor_profile,
            day_of_week=weekday
        )
        shifts_by_day[weekday] = shifts



    # Filter for admitting patients
    admitting_patients_visits = InpatientVisit.objects.filter(
        admitting_doctor=request.user.doctor_profile, discharge_date__isnull=True)

    # Filter for surgeries
    upcoming_surgeries = Surgery.objects.filter(
    scheduled_time__gt=timezone.now()
).filter(
    Q(lead_doctor=request.user.doctor_profile) |
    Q(assisting_doctors=request.user.doctor_profile)
).distinct()

    context = {
        'pname': "Duty",
        'user': request.user,
        'shifts_by_day': shifts_by_day,
        'admitting_patients_visits': admitting_patients_visits,
        'upcoming_surgeries': upcoming_surgeries,
    }
    return render(request, "duty.html", context)



def pharmacy_view(request):
    medicine_list = Medicine.objects.all()
    paginator = Paginator(medicine_list,1000) 
    page = request.GET.get('page')  
    medicines = paginator.get_page(page) 

    start,end = page_sort(medicines)
    context = {
        'pname': "Pharmacy",
        'user': request.user,
        'medicines': medicines,
        'start_page':start,
        'end_page':end,
    }
    return render(request, 'pharmacy.html', context)

################################################################################################
################################################################################################


@require_POST
def update_color_index(request):
    data = json.loads(request.body)
    request.user.color_index = data.get('color_index')
    request.user.save()
    return JsonResponse({'status': 'success'})



@require_POST
def update_color2_index(request):
    data = json.loads(request.body)
    request.user.color2_index = data.get('color_index')
    request.user.save()
    return JsonResponse({'status': 'success'})