import random
from datetime import datetime, timedelta, time
from django.core.management.base import BaseCommand
from backbone.models import DoctorVisit, Doctor, InpatientVisit

class Command(BaseCommand):
    help = 'Generate random doctor visits'

    def add_arguments(self, parser):
        parser.add_argument('--num_visits', type=int, default=100, help='Number of doctor visits to generate')

    def handle(self, *args, **kwargs):
        num_visits = kwargs['num_visits']
        self.stdout.write(f"Generating {num_visits} doctor visits")

        for _ in range(num_visits):
            self.generate_visit()

    def generate_visit(self):
        inpatient_visit = random.choice(InpatientVisit.objects.all())
        admission_date = inpatient_visit.admission_date
        discharge_date = inpatient_visit.discharge_date or datetime.now()

        # Random date within inpatient visit duration
        start_date = admission_date
        end_date = discharge_date
        if start_date >= end_date:
            return

        visit_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        visit_hour = random.randint(0, 23)
        visit_minute = random.randint(0, 59)
        visit_time = time(visit_hour, visit_minute)
        scheduled_visit = datetime.combine(visit_date, visit_time)

        # Selecting a non-surgeon doctor who is not on shift
        doctors = Doctor.objects.exclude(
            Q(speciality__name__icontains='surgeon') | 
            Q(subspecialities__name__icontains='surgeon')
        )
        doctor = self.select_doctor(doctors, scheduled_visit)
        if not doctor:
            return

        DoctorVisit.objects.create(
            doctor=doctor,
            inpatient_visit=inpatient_visit,
            visit_date=scheduled_visit,
            # ... other fields ...
        )

    def select_doctor(self, doctors, visit_time):
        for doctor in doctors:
            if self.is_doctor_off_duty(doctor, visit_time):
                return doctor
        return None

    def is_doctor_off_duty(self, doctor, visit_time):
        day_of_week = visit_time.strftime('%A')
        return not doctor.work_shifts.filter(
            day_of_week=day_of_week,
            shift_start_time__lte=visit_time.time(),
            shift_end_time__gte=visit_time.time()
        ).exists()




import random
from datetime import datetime, timedelta, time
from django.core.management.base import BaseCommand
from django.db.models import Q
from backbone.models import DoctorVisit, Doctor, InpatientVisit

class Command(BaseCommand):
    help = 'Generate random doctor visits'

    def add_arguments(self, parser):
        parser.add_argument('--num_visits', type=int, default=100, help='Number of doctor visits to generate')

    def handle(self, *args, **kwargs):
        num_visits = kwargs['num_visits']
        self.stdout.write(f"Generating {num_visits} doctor visits")

        for _ in range(num_visits):
            self.generate_visit()

    def generate_visit(self):
        inpatient_visit = random.choice(InpatientVisit.objects.all())
        admission_date = inpatient_visit.admission_date
        discharge_date = inpatient_visit.discharge_date or datetime.now()

        # Random date within inpatient visit duration
        visit_date = admission_date + timedelta(days=random.randint(0, (discharge_date - admission_date).days))
        visit_hour = random.randint(8, 17)  # Assuming visiting hours are between 8 AM and 5 PM
        visit_minute = random.randint(0, 59)
        visit_time = time(visit_hour, visit_minute)
        scheduled_visit = datetime.combine(visit_date, visit_time)

        # Selecting a non-surgeon doctor who is not on shift and not overlapping with other visits
        doctors = Doctor.objects.exclude(
            Q(speciality__name__icontains='surgeon') | 
            Q(subspecialities__name__icontains='surgeon')
        )
        doctor = self.select_doctor(doctors, scheduled_visit)
        if not doctor:
            return

        # Generate other fields randomly or with default values
        symptoms = "Patient reported severe abdominal pain and nausea."
        exam_results =  "Blood pressure: 120/80 mmHg, Heart rate: 78 bpm, No visible signs of distress."
        diagnosis = "Acute appendicitis."
        medications = "Paracetamol 500mg every 6 hours, Ondansetron 4mg as needed for nausea."
        treatment_plan =  "Recommended surgical consultation for potential appendectomy. IV fluids to be administered."
        notes =  "Patient stable, but requires urgent surgical evaluation."
        follow_up =  "Follow-up in 3 days post-surgery or earlier if symptoms worsen."
        instructions = "Maintain hydration and adhere to prescribed medication regimen. Seek immediate care if experiencing increased pain."
        duration = timedelta(minutes=random.randint(15, 30))
        is_emergency = random.choice([True, False])

        DoctorVisit.objects.create(
            doctor=doctor,
            inpatient_visit=inpatient_visit,
            visit_date=scheduled_visit,
            symptoms_presented=symptoms,
            physical_examination_results=exam_results,
            diagnosis=diagnosis,
            prescribed_medications=medications,
            treatment_plan=treatment_plan,
            doctor_notes=notes,
            follow_up_recommendations=follow_up,
            additional_instructions=instructions,
            visit_duration=duration,
            is_emergency=is_emergency
        )

    def select_doctor(self, doctors, visit_time):
        for doctor in doctors:
            if self.is_doctor_available(doctor, visit_time):
                return doctor
        return None

    def is_doctor_available(self, doctor, visit_time):
        # Check if doctor is not on shift
        day_of_week=visit_time.strftime('%A')
        if doctor.work_shifts.filter(
            day_of_week=day_of_week,
            shift_start_time__lte=visit_time.time(),
            shift_end_time__gte=visit_time.time()
        ).exists():
            return False

        # Check for overlapping visits
        return not DoctorVisit.objects.filter(
            doctor=doctor,
            visit_date__day=visit_time.day,
            visit_date__month=visit_time.month,
            visit_date__year=visit_time.year
        ).exists()
