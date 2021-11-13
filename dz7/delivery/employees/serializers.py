from rest_framework import serializers

from clients.models import Client
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'job', 'status', 'user']