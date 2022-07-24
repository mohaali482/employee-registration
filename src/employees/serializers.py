from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField("employee-detail")

    class Meta:
        model = Employee
        fields = "__all__"
