from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeUpdateSerializer


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = Employee(request.data)
            employee.save()
            serializer = EmployeeSerializer(employee)
            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        updateSerializer = EmployeeUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Employee.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        updateSerializer = EmployeeUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Employee.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({"status": "success", "data": None, "message": None})
