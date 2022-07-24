from rest_framework import viewsets, permissions

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
