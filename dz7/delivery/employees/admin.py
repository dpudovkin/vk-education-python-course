from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from employees.models import Employee


@admin.register(Employee)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("job","status","view_user")
    list_filter = ("job", "status")

    def view_user(self, obj):
        user = obj.user_id
        url = (
            reverse("admin:users_user_changelist")
            + "?"
            + urlencode({"users__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, user)
