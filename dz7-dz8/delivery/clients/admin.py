from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "home_address", "status")
    list_filter = ("status",)
