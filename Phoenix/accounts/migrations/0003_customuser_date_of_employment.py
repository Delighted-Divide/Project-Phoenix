# Generated by Django 4.2.5 on 2023-10-07 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_employment',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
