from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from clients.models import Client


@admin.register(Client)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user_id", "view_home_address", "status")
    list_filter = ("status",)

    def view_user(self, obj):
        user = obj.user_id
        url = (
                reverse("admin:users_user_changelist")
                + "?"
                + urlencode({"users__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, user)

    def view_home_address(self, obj):
        address = obj.home_address
        url = (
                reverse("admin:orders_address_changelist")
                + "?"
                + urlencode({"addresses__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, address)

