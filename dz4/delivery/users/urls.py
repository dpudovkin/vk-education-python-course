from django.contrib import admin
from django.urls import path, include
from users.views import user_list, user_info, create_user

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<username>/', user_info, name='user_info'),
    path('new/', create_user)
]