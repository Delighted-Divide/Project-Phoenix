from django.core.management.base import BaseCommand
from accounts.models import HospitalStaff, NameList, LastName
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Auto-generate non-doctor hospital staff members'

    def add_arguments(self, parser):
        # Add arguments for each job role
        parser.add_argument('--nurse', type=int, default=0)
        parser.add_argument('--administrator', type=int, default=0)
        parser.add_argument('--technician', type=int, default=0)
        parser.add_argument('--clerk', type=int, default=0)
        parser.add_argument('--janitor', type=int, default=0)
        parser.add_argument('--pharmacist', type=int, default=0)
        parser.add_argument('--therapist', type=int, default=0)
        parser.add_argument('--radiologist', type=int, default=0)
        parser.add_argument('--lab_technician', type=int, default=0)
        parser.add_argument('--receptionist', type=int, default=0)
        parser.add_argument('--maintenance_worker', type=int, default=0)
        parser.add_argument('--it_specialist', type=int, default=0)
        parser.add_argument('--counselor', type=int, default=0)
        parser.add_argument('--all', type=int, default=0)

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Salary base for each job role
        salary_base = {
            'Nurse': 40000, 'Administrator': 50000, 'Technician': 35000,
            'Clerk': 30000, 'Janitor': 25000, 'Pharmacist': 60000,
            'Therapist': 45000, 'Radiologist': 70000, 'Lab Technician': 40000,
            'Receptionist': 28000, 'Maintenance Worker': 27000,
            'IT Specialist': 55000, 'Counselor': 35000
        }

        # Creating staff for each job role
        for job_role in salary_base.keys():
            count = kwargs.get(job_role.lower(), 0) + kwargs['all'] # Get the count for the job role from arguments
            for _ in range(count):
                name_entry = NameList.objects.order_by('?').first()
                last_name_entry = LastName.objects.order_by('?').first()

                experience_years = random.randint(0, 50)
                salary = salary_base[job_role] + (experience_years * 1000)  # Increment salary based on experience

                staff_member = HospitalStaff(
                    first_name=name_entry.name if name_entry else faker.first_name(),
                    last_name=last_name_entry.name if last_name_entry else faker.last_name(),
                    gender=name_entry.gender if name_entry else random.choice(['Male', 'Female', 'Other']),
                    address=faker.address(),
                    phone_number=str(f"{faker.phone_number()}")[:10],
                    birthday=faker.date_of_birth(minimum_age=22, maximum_age=60),
                    city=faker.city(),
                    country=faker.country(),
                    nationality=faker.country(),
                    language=faker.language_name(),
                    marital_status=random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'Other']),
                    job_role=job_role.replace('_', ' ').title(),
                    experience_years=experience_years,
                    salary=salary,
                    image=None  # Or use Faker to generate an image URL
                )
                staff_member.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated non-doctor hospital staff members'))
