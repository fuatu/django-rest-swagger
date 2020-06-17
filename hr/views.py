from rest_framework import viewsets
from hr.serializers import EmployeeSerializer
from hr.models import Employee


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given employee.

    list:
    Return a list of all the existing employees.

    create:
    Create a new employee instance.

    update:
    Update an employee

    partial_update:
    Partial update an employee

    delete:
    Delete an employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer