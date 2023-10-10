from django.core.management.base import BaseCommand
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = 'Backup the database and then run migrations'

    def handle(self, *args, **kwargs):
        # Backup database (this example is for MySQL, adjust for your DB)
        os.system('mysqldump -u root -p IamHuman@123 phoenix > backup.sql')
