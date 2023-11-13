from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from accounts.models import CustomUser
from django.core import serializers
from django.http import JsonResponse
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