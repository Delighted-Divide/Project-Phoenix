from django.core.management.base import BaseCommand
from accounts.models import ElectricityBill, WaterBill
from backbone.models import InpatientVisit, Surgery
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Generate electricity and water bills based on hospital occupancy and surgeries'

    def add_arguments(self, parser):
        parser.add_argument('--months', type=int, default=6)

    def handle(self, *args, **kwargs):
        months = kwargs['months']
        start_date = datetime.now() - timedelta(days=30 * months)
        end_date = datetime.now()

        daily_avg_electricity_use = 1500  # Average kWh used per day
        daily_avg_water_use = 25000  # Average liters used per day

        current_date = start_date
        while current_date <= end_date:
            # Count the number of patients in the hospital on the current day
            patients_count = InpatientVisit.objects.filter(
                admission_date__lte=current_date,
                discharge_date__gte=current_date
            ).count()

            # Count the number of surgeries on the current day
            surgeries_count = Surgery.objects.filter(
                scheduled_time__date=current_date
            ).count()

            # Calculate total kWh and liters used
            total_kwh = (daily_avg_electricity_use + (patients_count * 10) + (surgeries_count * 20))* random.uniform(0.9,1.2)
            total_liters = (daily_avg_water_use + (patients_count * 100) + (surgeries_count * 200))* random.uniform(0.9,1.2)

            # Generate electricity bill
            ElectricityBill.objects.create(
                date_issued=current_date,
                total_kwh=total_kwh,
                cost_per_kwh=0.15,  # Set a fixed cost per kWh
                total_cost=total_kwh * 0.15
            )

            # Generate water bill
            WaterBill.objects.create(
                date_issued=current_date,
                total_liters=total_liters,
                cost_per_liter=0.001,  # Set a fixed cost per liter
                total_cost=total_liters * 0.001
            )

            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS('Successfully generated electricity and water bills'))
