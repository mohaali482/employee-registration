from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    birthDate = serializers.DateField(source='birth_date')
    martialStatus = serializers.CharField(source='martial_status')
    ssnCode = serializers.CharField(source='ssn_code')
    postalCode = serializers.CharField(source='post_code')
    personalPhone = PhoneNumberField(source='personal_phone')
    homePhone = PhoneNumberField(source='home_phone')

    class Meta:
        model = Employee
        fields = (
            'id',
            'firstName',
            'lastName',
            'birthDate',
            'martialStatus',
            'ssnCode',
            'address',
            'city',
            'postalCode',
            'email',
            'personalPhone',
            'homePhone',
            'created_date',
            'image',
        )
