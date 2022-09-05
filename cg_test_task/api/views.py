from rest_framework import viewsets

from api.serializers import EmployeeSerializer, JobRelationSerializer
from employees.models import Employee, JobRelation


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobRelation.objects.all()
    serializer_class = JobRelationSerializer
