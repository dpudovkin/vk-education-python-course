from django.contrib import admin

from orders.models import Order, Address

admin.site.register(Order)
admin.site.register(Address)