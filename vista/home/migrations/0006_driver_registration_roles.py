# Generated by Django 5.1.1 on 2024-12-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_driver_registration_confirm_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_registration',
            name='Roles',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
