from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from application import views
from clients.views import ClientViewSet
from employees.views import EmployeeViewSet
from orders.views import AddressViewSet, OrderViewSet
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'api/clients', ClientViewSet, basename='clients')
router.register(r'api/employees', EmployeeViewSet, basename='employees')
router.register(r'api/orders', OrderViewSet, basename='orders')
router.register(r'api/addresses', AddressViewSet, basename='addresses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social'))
]

urlpatterns += router.urls
