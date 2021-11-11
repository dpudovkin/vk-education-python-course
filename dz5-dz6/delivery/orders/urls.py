from django.urls import path, include

from orders.views import order_list, new_address, addresses, address_list, new_order, orders

urlpatterns = [
    path('', order_list),
    path('<int:order_id>/', orders),
    path('new/', new_order),
    path('addresses/', address_list),
    path('addresses/<int:address_id>', addresses),
    path('addresses/new/', new_address)
]