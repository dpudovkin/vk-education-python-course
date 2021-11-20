from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'job', 'status', 'user']


class EmployeeUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    job = serializers.CharField()
    status = serializers.CharField()
    user = serializers.IntegerField()

    def validate(self, data):
        user = data['user']
        errors = {}
        if Employee.objects.filter(user=user).exclude(id=data['id']).exists():
            errors['user'] = 'User id is not unique'
            raise ValidationError(errors)
        return data
