# Generated by Django 4.2.5 on 2023-10-07 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_experience', models.PositiveIntegerField(blank=True)),
                ('certifications', models.PositiveIntegerField(default=0, help_text='Number of certifications')),
                ('publications_count', models.PositiveIntegerField(default=0)),
                ('awards_count', models.PositiveIntegerField(default=0)),
                ('conferences_attended_count', models.PositiveIntegerField(default=0)),
                ('seminars_attended_count', models.PositiveIntegerField(default=0)),
                ('degrees', models.ManyToManyField(to='backbone.degree')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='backbone.specialist')),
                ('subspecialities', models.ManyToManyField(blank=True, related_name='doctors_subspecialities', to='backbone.specialist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'user__date_of_employment',
            },
        ),
    ]
