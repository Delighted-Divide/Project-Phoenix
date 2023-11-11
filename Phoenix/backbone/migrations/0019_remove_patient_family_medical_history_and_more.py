# Generated by Django 4.2.5 on 2023-11-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backbone', '0018_alter_room_options_remove_patient_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='family_medical_history',
        ),
        migrations.AlterField(
            model_name='patient',
            name='alternate_phone_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
