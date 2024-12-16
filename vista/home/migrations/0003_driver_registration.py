# Generated by Django 5.1.1 on 2024-11-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_registration_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('Password', models.CharField(max_length=40, null=True)),
                ('Confirm_Password', models.CharField(max_length=40, null=True)),
                ('image', models.ImageField(null=True, upload_to='img')),
            ],
        ),
    ]