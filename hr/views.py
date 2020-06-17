from rest_framework import viewsets
from hr.serializers import EmployeeSerializer
from hr.models import Employee


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer