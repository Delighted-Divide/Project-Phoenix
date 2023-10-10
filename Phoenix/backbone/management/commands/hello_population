from django.core.management.base import BaseCommand, CommandError
from backbone.models import Lab


class Command(BaseCommand):
    help = 'Populate the database with initial lab data'

    def handle(self, *args, **kwargs):
        hospital_labs = [
            "Radiology lab",
            "Pathology Lab",
            "Cardiology Lab",
            "Neurology Lab",
            "Pulmonary Function Lab",
            "Endoscopy Suite",
            "Nuclear Medicine lab",
            "Microbiology Lab",
            "Hematology Lab",
            "Biochemistry Lab",
            "Genetics Lab",
            "Immunology Lab",
            "Cytology Lab",
            "Molecular Diagnostics Lab",
            "Virology Lab",
            "Mycology Lab",
            "Parasitology Lab",
            "Toxicology Lab",
            "Histology Lab",
            "Phlebotomy Lab"
        ]

        try:
            labs = [Lab(name=lab) for lab in hospital_labs]
            Lab.objects.bulk_create(labs)
        except Exception as e:
            raise CommandError(f"Error occured: {e}")
        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {Lab.objects.count()} users!'))
