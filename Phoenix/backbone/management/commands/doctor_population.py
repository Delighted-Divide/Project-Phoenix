from django.core.management import BaseCommand
from accounts.models import CustomUser
from backbone.models import *
import random
import string
import requests
import math
from django.db.models import Count


class Command(BaseCommand):
    help = 'Creates a specified number of Doctor profiles with random fields'

    def add_arguments(self, parser):
        parser.add_argument('num_doctors', type=int,
                            help='The number of Doctor profiles to create')

    def handle(self, *args, **options):
        num_doctors = options['num_doctors']

        for _ in range(num_doctors):
            users = CustomUser.objects.annotate(
                doctor_count=Count('doctor_profile')).filter(doctor_count=0)
            user = random.choice(users)

            years_of_experience = random.randint(0, 40)

            k1, k2, k3, k4, k5 = 2, 1, 3, 2.5, 1.5

            multiplier_c, multiplier_a, multiplier_conf, multiplier_sem, multiplier_pub = [
                random.uniform(0, 1.5) for _ in range(5)]

            Certificate = k1 * years_of_experience * multiplier_c
            Award = k2 * math.sqrt(years_of_experience) * multiplier_a
            Conference = k3 * \
                math.log(years_of_experience + 1) * multiplier_conf
            Seminar = k4 * math.log(years_of_experience + 1) * multiplier_sem
            Publication = k5 * (years_of_experience / 5) * multiplier_pub

            no_of_degree = random.choices([1, 2, 3], k=1, weights=[9, 4, 1])[0]
            no_of_subspeciality = random.choices(
                [1, 2, 3, 4], k=1, weights=[16, 9, 4, 1])[0]
            degree = random.choices(Degree.objects.all(), k=no_of_degree)
            speciality = random.choice(Specialist.objects.all())
            subspecialities = Specialist.objects.exclude(id=speciality.id)
            subspeciality = random.choices(
                subspecialities, k=no_of_subspeciality)

            # Create the Doctor profile
            doctor = Doctor.objects.create(
                user=user,
                years_of_experience=years_of_experience,  # Random years between 1 and 40
                speciality=speciality,
                # Random certifications between 0 and 10
                certifications=Certificate,
                publications_count=Publication,
                awards_count=Award,
                conferences_attended_count=Conference,
                seminars_attended_count=Seminar
            )

            # Add the Degree to the Doctor's degrees many-to-many field
            doctor.degrees.add(*degree)

            # Add a subspeciality if it exists
            if subspeciality:
                doctor.subspecialities.add(*subspeciality)

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created doctor profile for user {user.id}'))
