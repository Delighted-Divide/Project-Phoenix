import random
from datetime import time, timedelta
from django.core.management.base import BaseCommand
from backbone.models import Doctor, DoctorWorkShift

class Command(BaseCommand):
    help = 'Generates work shifts for all doctors'

    def add_arguments(self, parser):
        parser.add_argument('--num_doctors', type=int, help='Number of doctors to generate shifts for')

    def handle(self, *args, **kwargs):
        num_doctors = kwargs['num_doctors']
        doctors = Doctor.objects.all()[:num_doctors] if num_doctors else Doctor.objects.all()
        days = [day[0] for day in DoctorWorkShift.WeekDay.choices]

        for doctor in doctors:
            # Initialize a schedule map for the week
            schedule_map = {day: [] for day in days}

            total_hours = random.randint(20, 50)  # Total weekly hours
            num_shifts = random.randint(10, 14)  # Increase number of shifts
            hours_per_shift = total_hours // num_shifts
            extra_hours = total_hours % num_shifts

            shift_hours = [hours_per_shift + (1 if i < extra_hours else 0) for i in range(num_shifts)]
            random.shuffle(shift_hours)  # Distribute hours randomly across shifts

            for shift_length in shift_hours:
                shift_assigned = False

                while not shift_assigned:
                    day = random.choice(days)
                    start_hour = random.randint(0, 23)
                    end_hour = (start_hour + shift_length) % 24

                    # Check for overlap
                    if not self.is_overlap(schedule_map[day], start_hour, end_hour):
                        shift = DoctorWorkShift(
                            doctor=doctor,
                            day_of_week=day,
                            shift_start_time=time(start_hour, 0),
                            shift_end_time=time(end_hour, 0)
                        )
                        shift.save()
                        schedule_map[day].append((start_hour, end_hour))
                        shift_assigned = True

        self.stdout.write(self.style.SUCCESS('Successfully generated work shifts for all doctors'))

    def is_overlap(self, shifts, start_hour, end_hour):
        for shift_start, shift_end in shifts:
            if start_hour < shift_end and end_hour > shift_start:
                return True
        return False