import mysql.connector
from django.core.management.base import BaseCommand
from accounts.models import Medicine

class Command(BaseCommand):
    help = 'Imports medicines data from another MySQL database'

    def handle(self, *args, **kwargs):

        # Connect to the database
        connection = mysql.connector.connect(
                    host= "localhost",
                    user = "root",
                    password = "IamHuman@123",
                    database = "company"
                )
        cursor = connection.cursor()

        # SQL query to fetch data
        query = "SELECT DISTINCT name, price, prescription, package, manufacturer, composition FROM medicines"
        cursor.execute(query)

        for (name, raw_price, prescription, package, manufacturer, composition) in cursor:
            price = round(float(raw_price.replace('MRP₹', '')) / 100,2)
            prescription_required = 'Prescription Required' in prescription

            Medicine.objects.update_or_create(
                name=name,
                defaults={
                    'price': price,
                    'prescription_required': prescription_required,
                    'package': package,
                    'manufacturer': manufacturer,
                    'composition': composition
                }
            )

        cursor.close()
        connection.close()

        self.stdout.write(self.style.SUCCESS('Successfully imported medicines data'))
