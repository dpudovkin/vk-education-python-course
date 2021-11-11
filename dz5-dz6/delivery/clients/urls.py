from django.urls import path

from clients.views import clients_list, clients, new_client

urlpatterns = [
    path('', clients_list),
    path('<int:employee_id>/', clients),
    path('new/', new_client),
]