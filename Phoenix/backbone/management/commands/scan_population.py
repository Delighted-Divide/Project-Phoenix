from django.core.management.base import BaseCommand, CommandError
from backbone.models import ScanTest, Lab


class Command(BaseCommand):
    help = 'Populate the database with initial scan data'

    def handle(self, *args, **kwargs):
        labs_and_centers = {
            "Radiology lab": {
                "CT Scan": 300,
                "MRI Scan": 500,
                "X-Ray": 60,
                "X-Ray Skeletal Survey": 150,
                "Sonography (Ultrasound / USG)": 100,
                "Sonomamography / Sonomamogram": 120,
                "4D Scan": 120
            },
            "Nuclear Medicine lab": {
                "Bone Scan": 250,
                "DMSA Scan": 200,
                "Gallium Scan": 350,
                "HIDA Scan": 250,
                "MIBG Scan": 300,
                "MUGA Scan": 250,
                "Thallium Scan": 300,
                "Thyroid Scan": 150,
                "PET-CT Scan": 600,
                "VQ Scan (Lung Ventilation and Lung Perfusion Scan)": 300
            },
            "Cardiology Lab": {
                "Stress Echo Test": 180,
                "Doppler Ultrasound": 150
            }
        }

        try:
            scan = [ScanTest(name=scan, price=price*15, lab=Lab.objects.get(name=lab)) for lab,
                    scans in labs_and_centers.items() for scan, price in scans.items()]
            ScanTest.objects.bulk_create(scan)
        except Exception as e:
            raise CommandError(f"Error occured: {e}")
        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {ScanTest.objects.count()} scans!'))
