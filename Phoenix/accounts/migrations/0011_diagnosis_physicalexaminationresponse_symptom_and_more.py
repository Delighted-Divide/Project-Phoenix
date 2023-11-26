# Generated by Django 4.2.5 on 2023-11-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_hobby_alter_customuser_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('recommended_specialist', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExaminationResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('response_type', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255, verbose_name='Recommended Specialist')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='color2_index',
            field=models.IntegerField(default=2, editable=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='color_index',
            field=models.IntegerField(default=1, editable=False),
        ),
    ]
