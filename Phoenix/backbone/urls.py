from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name="Dashboard"),
    path('doctor/', views.doctor, name="Doctor"),
    path('profile/<uuid:user_id>/', views.doctor_profile, name='profile'),
    path('addDoctor/', views.register, name="addDoc"),
    path('patient/', views.patient, name="Patient"),
    path('room/', views.room, name="Room"),
    path('surgery/', views.surgery, name="Surgery"),
    path('appointment/', views.appointment, name="Appointment"),
    path('laboratory/', views.laboratory, name="Laboratory"),
    path('laboratory/<lab_name>/', views.lab, name="Lab"),
    path('duty/', views.duty, name="Duty"),
    path('update-color-index/', views.update_color_index, name='update_color_index'),
    path('update-color2-index/', views.update_color2_index, name='update_color2_index'),
    path('pharmacy/', views.pharmacy_view, name='Pharmacy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
