from django.core.management.base import BaseCommand
from backbone.models import Patient
from accounts.models import NameList,LastName
from random import choice, randint
from faker import Faker
import string
from datetime import date


class Command(BaseCommand):
    help = 'Generate random patient records'

    def add_arguments(self, parser):
        parser.add_argument('num_patients', type=int,
                            help='Number of patient records to create')

    def handle(self, *args, **kwargs):
        def generate_random_patient():


            random_name_id = randint(1, 7203)
            random_name_entry = NameList.objects.get(id=random_name_id)
            selected_name = random_name_entry.name
            selected_gender = random_name_entry.gender


            random_last_name_id = randint(1, 473)
            random_last_name_entry = LastName.objects.get(id=random_last_name_id)
            selected_last_name = random_last_name_entry.name


            email = f"{selected_name+selected_last_name}@email.com"
            while Patient.objects.filter(email=email):
                random_number = randint(1,999)
                email = f"{selected_name+selected_last_name+str(random_number)}@email.com"
            fake = Faker()
            marital_status = choice(['S', 'M', 'D', 'W'])
            blood_type = choice(
                ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
            
            phone_number = fake.phone_number()[:20]
            alternate_phone_number = fake.phone_number()[:20]
            pin = fake.zipcode()

            patient = Patient(
                first_name=selected_name,
                last_name=selected_last_name,
                date_of_birth=fake.date_of_birth(
                    minimum_age=19, maximum_age=115),
                gender=selected_gender,
                nationality=fake.country()[:50] ,
                language_spoken=choice(["English", "Spanish", "Mandarin"]),
                address=fake.address()[:-5] + pin,
                city=fake.city()[:50],
                state=fake.state()[:50],
                zip_code=pin,
                country="US",
                phone_number=phone_number,
                alternate_phone_number = alternate_phone_number,
                email=email,
                marital_status=marital_status,
                occupation=fake.job(),
                blood_type=blood_type
            )
            return patient
        for _ in range(kwargs['num_patients']):
            patient = generate_random_patient()
            patient.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added {patient}'))
        self.stdout.write(self.style.SUCCESS('Successfully populated patients in the database'))