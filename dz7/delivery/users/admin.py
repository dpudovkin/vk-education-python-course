from django.contrib import admin

from users.models import User


@admin.register(User)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_day", "phone_number")
