from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from backbone.models import InpatientVisit, Patient,Bed,Doctor
import random


class Command(BaseCommand):
    help = 'Generate random inpatient visits with static data, ensuring no patient repetition'

    def add_arguments(self, parser):
        parser.add_argument('--num_visits', type=int, default=10, help='Number of inpatient visits to generate')

    def handle(self, *args, **kwargs):
        num_visits = kwargs['num_visits']
        self.stdout.write(f"Generating {num_visits} inpatient visits")

        patients = list(Patient.objects.all())
        if len(patients) < num_visits:
            self.stdout.write(self.style.ERROR("Not enough patients to generate the requested number of visits."))
            return

        for _ in range(num_visits):
            patient = random.choice(patients)
            patients.remove(patient)  # Remove the patient to prevent repetition
            self.create_inpatient_visit(patient)

    def create_inpatient_visit(self, patient):
        available_bed = self.get_available_bed()
        if not available_bed:
            self.stdout.write(self.style.WARNING(f"No available bed for patient {patient}."))
            return
        InpatientVisit.objects.create(
            patient=patient,
            admitting_doctor=Doctor.objects.order_by("?").first(), 
            admission_date=timezone.now(),
            discharge_date=None,
            bed=available_bed,
            reason_for_admission="High fever and persistent cough",
            initial_diagnosis="Suspected pneumonia",
            final_diagnosis="Bacterial pneumonia",
            medical_history="Diabetes mellitus",
            surgical_history=None,
            medication_history="Metformin",
            organ_donor=False,
            tobacco_use=False,
            alcohol_use=False,
            allergies="Sulfa drugs",
            current_medications="Amoxicillin",
            treatment_plan="Antibiotic therapy and glucose monitoring",
            complications="Elevated blood sugar levels",
            prognosis="Good, with antibiotic completion",
            follow_up_instructions="Complete antibiotic course, monitor blood sugar",
            next_follow_up_date=timezone.now() + timedelta(days=20),
            insurance_provider="MediSecure",
            insurance_policy_number="MS123456789",
            emergency_contact_name="Alice Johnson",
            emergency_contact_phone="321-654-0987",
            emergency_contact_relationship="Daughter",
            notes="Patient responded well to treatment, blood sugar to be monitored closely")
        self.stdout.write(f"Inpatient visit created for patient {patient}.")

    def get_available_bed(self):
        available_beds = Bed.objects.filter(is_occupied=False)
        return available_beds.first() if available_beds.exists() else None