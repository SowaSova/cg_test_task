from api.serializers import EmployeeSerializer, JobRelationSerializer
from employees.models import Employee, JobRelation
from rest_framework import pagination, viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = pagination.LimitOffsetPagination


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobRelation.objects.all()
    serializer_class = JobRelationSerializer
    pagination_class = pagination.LimitOffsetPagination
