# Generated by Django 3.2.14 on 2022-08-07 09:39

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('birth_date', models.DateField(verbose_name='Birthdate')),
                ('martial_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=10, verbose_name='Martial Status')),
                ('ssn_code', models.CharField(max_length=250, verbose_name='SSN code')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('city', models.CharField(max_length=250, verbose_name='City')),
                ('post_code', models.CharField(max_length=12, verbose_name='Post Code')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('personal_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('image', models.ImageField(upload_to='employees/employee/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
    ]
