# Generated by Django 4.2.5 on 2023-10-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics\\_Pure_as_Snow__White_Fashion_Delight_.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
