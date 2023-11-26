# Generated by Django 4.2.5 on 2023-11-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backbone', '0027_icu_rename_surgery_name_surgery_surgery_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icu',
            options={'ordering': ['Label']},
        ),
        migrations.AddField(
            model_name='doctor',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('fired', 'Fired'), ('retired', 'Retired'), ('on_duty', 'On Duty'), ('resigned', 'Resigned'), ('not_on_duty', 'Not on Duty')], default='not_on_duty', max_length=20),
        ),
    ]
