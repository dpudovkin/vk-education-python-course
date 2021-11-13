from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from orders.models import Order, Address

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "cost", "comment", "status", "view_performer", "base_award")
    list_filter = ("status","performer_id")
    list_select_related = ("destination_client_id", "arriving_client_id")

    def view_performer(self, obj):
        employee = obj.performer_id
        url = (
            reverse("admin:employees_employee_changelist")
            + "?"
            + urlencode({"employees__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, employee)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "longitude", "latitude")

