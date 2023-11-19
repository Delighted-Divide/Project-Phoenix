from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
import random
from django.db.models import Q
from backbone.models import Doctor, Patient, Appointment, DoctorWorkShift, InpatientVisit

class Command(BaseCommand):
    help = 'Generate appointments for all doctors within their work shifts for the next week'

    def handle(self, *args, **kwargs):
        end_date = datetime.now().date() + timedelta(days=7)
        doctors = Doctor.objects.all()
        patients = self.get_available_patients()

        for doctor in doctors:
            self.create_appointments_for_doctor(doctor, end_date, patients)

    def get_available_patients(self):
        # Exclude patients with an active inpatient visit
        active_patients = InpatientVisit.objects.filter(
            discharge_date__isnull=True).values_list('patient', flat=True)
        return list(Patient.objects.exclude(id__in=active_patients))

    def create_appointments_for_doctor(self, doctor, end_date, patients):
        for work_shift in DoctorWorkShift.objects.filter(doctor=doctor):
            current_date = datetime.now().date()
            while current_date <= end_date:
                if work_shift.day_of_week == current_date.strftime('%A'):
                    for appointment_time in self.generate_appointment_times(work_shift):
                        if not self.is_time_slot_taken(doctor, current_date, appointment_time, patients):
                            patient = random.choice(patients)
                            self.create_appointment(doctor, patient, current_date, appointment_time)
                            patients.remove(patient)  # Remove patient to prevent multiple appointments
                current_date += timedelta(days=1)

    def generate_appointment_times(self, work_shift):
        times = []
        current_time = work_shift.shift_start_time
        while current_time < work_shift.shift_end_time:
            times.append(current_time)
            current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()
        return times

    def is_time_slot_taken(self, doctor, date, time, patients):
        # Check if time slot is taken
        if Appointment.objects.filter(doctor=doctor, appointment_date=date, start_time=time).exists():
            return True

        # Check if patient already has an appointment at this time
        patient_ids = [patient.id for patient in patients]
        return Appointment.objects.filter(
            patient_id__in=patient_ids, 
            appointment_date=date, 
            start_time__lte=time, 
            end_time__gte=time
        ).exists()

    def create_appointment(self, doctor, patient, date, start_time):
        end_time = (datetime.combine(date, start_time) + timedelta(minutes=30)).time()
        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=date,
            start_time=start_time,
            end_time=end_time,
            status=Appointment.AppointmentStatus.SCHEDULED
        )
