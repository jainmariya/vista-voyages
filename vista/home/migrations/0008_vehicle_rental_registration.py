# Generated by Django 5.1.1 on 2024-12-18 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_about_cab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_reg_number', models.CharField(max_length=20, null=True, unique=True)),
                ('vehicle_type', models.CharField(max_length=20, null=True)),
                ('make_model', models.CharField(max_length=100, null=True)),
                ('year_of_manufacture', models.PositiveIntegerField(null=True)),
                ('fuel_type', models.CharField(max_length=10, null=True)),
                ('transmission_type', models.CharField(max_length=10, null=True)),
                ('mileage', models.PositiveIntegerField(help_text='Mileage in kilometers', null=True)),
                ('engine_capacity', models.CharField(help_text='Engine capacity in liters', max_length=10, null=True)),
                ('rental_price_per_day', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('availability', models.BooleanField(default=True, null=True)),
                ('vehicle_image', models.ImageField(null=True, upload_to='vehicleimg')),
            ],
        ),
        migrations.CreateModel(
            name='rental_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=20)),
                ('aadhar', models.CharField(max_length=12)),
                ('license_image', models.ImageField(upload_to='licenseimg')),
                ('owner_image', models.ImageField(null=True, upload_to='ownerimg')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.vehicle')),
            ],
        ),
    ]