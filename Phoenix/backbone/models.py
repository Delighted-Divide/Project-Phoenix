from collections.abc import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
import uuid

# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(
        'accounts.CustomUser', on_delete=models.CASCADE, related_name='doctor_profile')
    # specialization = models.ManyToManyField('Specialization')
    # sub_specialization = models.ManyToManyField(
    #     'SubSpecialization', blank=True)
    years_of_experience = models.PositiveIntegerField(blank=True)
    degrees = models.ManyToManyField('degree')
    speciality = models.ForeignKey(
        'specialist', on_delete=models.CASCADE, related_name='doctors')
    subspecialities = models.ManyToManyField(
        'specialist', blank=True, related_name='doctors_subspecialities')
    certifications = models.PositiveIntegerField(default=0,
                                                 help_text="Number of certifications")

    # Professional Achievements
    publications_count = models.PositiveIntegerField(default=0)
    awards_count = models.PositiveIntegerField(default=0)
    conferences_attended_count = models.PositiveIntegerField(default=0)
    seminars_attended_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        user = str(self.user).title()
        return f"Dr. {user}"

    class Meta:
        get_latest_by = 'user__date_of_employment'


class Degree(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Specialist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    # Personal Details
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    language_spoken = models.CharField(
        max_length=50, blank=True, null=True, default="English")

    # Contact Details
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    alternate_phone_number = models.CharField(
        max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    # Medical Details
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100)
    family_medical_history = models.TextField(blank=True, null=True)
    blood_type = models.CharField(
        max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)

    # Miscellaneous
    profile_picture = models.ImageField(
        upload_to='patients/', default='profile_pics\_Pure_as_Snow__White_Fashion_Delight_.jpg')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class OutpatientVisit(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)

    # Basic checkup details
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Weight in kilograms")
    blood_pressure = models.CharField(
        max_length=10, help_text="Blood Pressure in mmHg, format: systolic/diastolic e.g., 120/80")
    temperature = models.DecimalField(
        max_digits=4, decimal_places=2, help_text="Temperature in Celsius")
    pulse_rate = models.PositiveIntegerField(
        help_text="Pulse rate in beats per minute")
    respiratory_rate = models.PositiveIntegerField(
        help_text="Respiratory rate in breaths per minute")
    oxygen_saturation = models.PositiveIntegerField(
        help_text="Oxygen saturation in percentage")
    tobacco_use = models.BooleanField(default=False)
    alcohol_use = models.BooleanField(default=False)

    # Medical history and complaints
    reason = models.TextField(help_text="Main reason for the visit")
    medical_history = models.TextField(
        blank=True, help_text="Patient's past medical history")
    surgical_history = models.TextField(blank=True, null=True)
    current_medications = models.TextField(
        blank=True, help_text="Current medications patient is taking")
    allergies = models.TextField(blank=True, help_text="Known allergies")

    # Examination findings and diagnosis
    physical_examination = models.TextField(
        default="Normal", help_text="Findings from physical examination")
    diagnosis = models.TextField(
        help_text="Doctor's diagnosis based on the visit")

    # Recommendations and follow-up
    treatment_plan = models.TextField(
        blank=True, help_text="Recommended treatment plan")
    follow_up_date = models.DateField(
        blank=True, null=True, help_text="Next scheduled visit, if any")
    additional_notes = models.TextField(
        blank=True, help_text="Any other notes or recommendations from the doctor")

    def __str__(self):
        return f"{self.patient} with {self.doctor} -- Visit on {self.visit_date.date()}"
