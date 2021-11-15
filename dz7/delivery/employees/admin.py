from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("job", "status", "user")
    list_filter = ("job", "status")
