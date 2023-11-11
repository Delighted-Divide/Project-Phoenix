from collections.abc import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import uuid
import string


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
    total_score = models.PositiveIntegerField(editable=False, default=0)

    def save(self, *args, **kwargs) -> None:
        w1, w2, w3, w4, w5 = 0.1, 0.3, 0.1, 0.2, 0.4
        total_score = w1 * self.certifications + w2 * self.awards_count + w3 * \
            self.conferences_attended_count + w4 * \
            self.seminars_attended_count + w5 * self.publications_count
        self.total_score = int(total_score)
        super().save(*args, **kwargs)

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
    phone_number = models.CharField(max_length=15,)
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

    def save(self, *args, **kwargs):
        # Check if the instance is being created (i.e., doesn't have a primary key yet)
        is_new = self._state.adding
        print(is_new)
        super().save(*args, **kwargs)
        Customer.objects.update_or_create(
            patient=self,
            defaults={
                'first_name': self.first_name,
                'last_name': self.last_name,
                'phone_number': self.phone_number,
                'email': self.email
            }
        )
        # if is_new:
        #     print("hello")
        #     # Create a corresponding Customer instance
        #     Customer.objects.create(
        #         first_name=self.first_name,
        #         last_name=self.last_name,
        #         phone_number=self.phone_number,
        #         email=self.email,
        #         patient=self
        #     )

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
    medications_prescribed = models.TextField(
        blank=True, help_text="Medication")
    follow_up_date = models.DateField(
        blank=True, null=True, help_text="Next scheduled visit, if any")
    additional_notes = models.TextField(
        blank=True, help_text="Any other notes or recommendations from the doctor")

    def __str__(self):
        return f"{self.patient} with {self.doctor} -- Visit on {self.visit_date.date()}"


class Room(models.Model):
    ROOM_TYPES = (
        ('GW', 'General Ward'),
        ('SP', 'Semi Private'),
        ('PR', 'Private'),
        ('DL', 'Delux'),
        ('KD', 'King\'s Delux'),
    )

    BED_COUNTS = {
        'GW': 8,
        'SP': 2,
        'PR': 1,
        'DL': 1,
        'KD': 1,
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)
    room_id = models.CharField(
        max_length=10, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        is_new = not self.room_id
        if not self.room_id:
            # Get the prefix from the room type
            prefix = self.room_type
            # Count the existing rooms of this type
            count = Room.objects.filter(room_type=self.room_type).count() + 1
            # Construct the room_id
            self.room_id = f"{prefix}{count:03}"
        super().save(*args, **kwargs)
        if is_new:
            # If it's a new room, create the beds for it
            bed_count = self.BED_COUNTS.get(self.room_type, 0)
            for i in range(bed_count):
                bed_label = string.ascii_uppercase[i]
                Bed.objects.create(bed_label=bed_label, room=self)

    def __str__(self) -> str:
        return f"{self.room_id}"

    class Meta:
        ordering = ['-room_type']


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_label = models.CharField(max_length=5, editable=False)
    is_occupied = models.BooleanField(default=False)

    class Meta:
        unique_together = ["room", "bed_label"]

    def __str__(self) -> str:
        return f"{self.room.room_id} - {self.bed_label}"


class DoctorVisit(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    inpatient_visit = models.ForeignKey(
        'InpatientVisit', on_delete=models.CASCADE)

    visit_date = models.DateTimeField(auto_now_add=True)
    symptoms_presented = models.TextField(
        help_text="Symptoms observed or reported by the patient during the visit.")
    physical_examination_results = models.TextField(
        blank=True, null=True, help_text="Results from the physical examination, e.g., heart rate, respiratory rate, etc.")
    diagnosis = models.CharField(max_length=255, blank=True, null=True,
                                 help_text="Preliminary or final diagnosis given by the doctor.")
    prescribed_medications = models.TextField(
        blank=True, null=True, help_text="Medications prescribed during the visit.")
    treatment_plan = models.TextField(
        blank=True, null=True, help_text="Detailed treatment plan or procedures to be followed.")
    doctor_notes = models.TextField(null=True, blank=True)
    follow_up_recommendations = models.TextField(null=True, blank=True)
    additional_instructions = models.TextField(
        blank=True, null=True, help_text="Any additional instructions given by the doctor to the patient.")
    visit_duration = models.DurationField(
        null=True, blank=True, help_text="Duration of the doctor's visit.")
    is_emergency = models.BooleanField(
        default=False, help_text="Indicates if the visit was due to an emergency situation.")

    def __str__(self):
        return f"Visit on {self.visit_date} by Dr. {self.doctor} for {self.inpatient_visit.patient}"


class InpatientVisit(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    admitting_doctor = models.ForeignKey(
        'Doctor', related_name='admissions', on_delete=models.SET_NULL, null=True, blank=True)
    bed = models.ForeignKey(
        'Bed', on_delete=models.SET_NULL, null=True)

    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)
    reason_for_admission = models.TextField(
        help_text="Primary reason for the patient's admission.")
    initial_diagnosis = models.TextField(
        blank=True, null=True, help_text="Initial diagnosis when the patient was admitted.")
    final_diagnosis = models.TextField(
        blank=True, null=True, help_text="Final diagnosis upon discharge or during the course of treatment.")
    medical_history = models.TextField(
        blank=True, null=True, help_text="Patient's past medical history.")
    surgical_history = models.TextField(
        blank=True, null=True, help_text="Any surgeries or operations the patient has undergone in the past.")
    medication_history = models.TextField(
        blank=True, null=True, help_text="List of medications the patient was on before admission.")
    organ_donor = models.BooleanField(default=False)
    tobacco_use = models.BooleanField(default=False)
    alcohol_use = models.BooleanField(default=False)
    allergies = models.TextField(
        blank=True, null=True, help_text="Any known allergies.")
    current_medications = models.TextField(
        blank=True, null=True, help_text="Medications prescribed during the hospital stay.")
    treatment_plan = models.TextField(
        blank=True, null=True, help_text="Detailed treatment plan or procedures followed during the stay.")
    complications = models.TextField(
        blank=True, null=True, help_text="Any complications that arose during the hospital stay.")
    prognosis = models.TextField(
        blank=True, null=True, help_text="Doctor's prognosis upon discharge.")
    follow_up_instructions = models.TextField(
        blank=True, null=True, help_text="Instructions for the patient to follow post-discharge.")
    next_follow_up_date = models.DateField(
        null=True, blank=True, help_text="Date for the next follow-up visit, if scheduled.")
    insurance_provider = models.CharField(max_length=255, blank=True)
    insurance_policy_number = models.CharField(max_length=255, blank=True)
    emergency_contact_name = models.CharField(
        max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(
        max_length=15, blank=True, null=True)
    emergency_contact_relationship = models.CharField(
        max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True,
                             help_text="Any additional notes or observations.")

    def clean(self):
        errors = {}
        active_visits = InpatientVisit.objects.filter(
            patient=self.patient, discharge_date=None)

        # If we're updating an existing record, exclude the current record from the query
        if self.pk:
            active_visits = active_visits.exclude(pk=self.pk)

        # If any active visits are found, raise a validation error
        if active_visits.exists():
            errors['patient'] = 'This patient already has an active InpatientVisit. A patient cannot have multiple active visits.'
        # Check if the bed is occupied
        if self.discharge_date:
            old_record = InpatientVisit.objects.get(pk=self.pk)
            if old_record.bed != self.bed:
                errors['bed'] = f'The given bed is {old_record.bed}. You cannot change the bed when a discharge date is entered.'
            # If only the discharge_date is given and bed hasn't changed
            self.bed.is_occupied = False
        elif self.pk:  # if the instance has a primary key, it's being edited
            org = InpatientVisit.objects.get(pk=self.pk)
            if org.bed != self.bed and self.bed.is_occupied:
                errors['bed'] = "The selected bed is already occupied."

        elif self.bed.is_occupied:  # for new instances
            errors['bed'] = "The selected bed is already occupied."

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if (self.pk and self.bed != InpatientVisit.objects.get(pk=self.pk).bed):
            old_record = InpatientVisit.objects.get(pk=self.pk)
            print(
                f"Moved from {old_record.bed} to {self.bed}")
            old_record.bed.is_occupied = False
            old_record.bed.save()
            self.bed.is_occupied = True
        elif not self.pk:
            print(f"{self.patient} in {self.bed}")
            self.bed.is_occupied = True

        super().save(*args, **kwargs)
        self.bed.save()

        # If a discharge date is entered, set the bed as unoccupied

    def delete(self, *args, **kwargs):
        print(f"{self} is being deleted")
        self.bed.is_occupied = False
        self.bed.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Inpatient Visit for {self.patient.first_name} {self.patient.last_name} on {self.admission_date}"


class Lab(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"


class LabTest(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lab = models.ForeignKey(
        Lab, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    patienttests = GenericRelation('patienttest')

    def __str__(self):
        return f"{self.name}"


class ScanTest(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lab = models.ForeignKey(
        Lab, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    patienttests = GenericRelation('PatientTest')

    def __str__(self):
        return f"{self.name}"


class PatientTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Fields for GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    test = GenericForeignKey('content_type', 'object_id')
    test_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    patient = models.OneToOneField(
        Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name="customer")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
