from django.urls import path

from employees.views import employees_list, employees, new_employee

urlpatterns = [
    path('', employees_list),
    path('<int:employee_id>/', employees),
    path('new/', new_employee),
]