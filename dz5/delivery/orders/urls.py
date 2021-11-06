from django.urls import path, include
from orders.views import order_list, order_info, create_order

urlpatterns = [
    path('', order_list, name='user_list'),
    path('<int:order_id>/', order_info, name='user_info'),
    path('new/', create_order)
]