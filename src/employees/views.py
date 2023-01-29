from django.core.cache import cache
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Employee.objects.all()
    model = Employee()
    filter_backends = [filters.SearchFilter]
    search_fields = ('first_name', 'last_name', 'city', 'email')
