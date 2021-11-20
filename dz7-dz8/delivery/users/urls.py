from django.urls import path

from users.views import user_list, user_info, create_user

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:user_id>/', user_info, name='user_info'),
    path('new/', create_user)
]
