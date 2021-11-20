from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from application.views import rest_login_is_required
from orders.models import Address, Order
from orders.serializers import AddressSerializer, OrderSerializer


class AddressViewSet(viewsets.ViewSet):

    @rest_login_is_required()
    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    @rest_login_is_required()
    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    @rest_login_is_required(staff_required=True)
    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = Address(**request.data)
            address.save()
            serializer = AddressSerializer(address)
            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def update(self, request, pk=None):
        address = get_object_or_404(Address.objects.all(), pk=pk)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            Address.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": serializer.data, "message": None})
        return Response({"status": "error", "errors": serializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def partial_update(self, request, pk=None):
        address = get_object_or_404(Address.objects.all(), pk=pk)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            Address.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": serializer.data, "message": None})
        return Response({"status": "error", "errors": serializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def destroy(self, request, pk=None):
        address = get_object_or_404(Address.objects.all(), pk=pk)
        address.delete()
        return Response({"status": "success", "data": None, "message": None})


class OrderViewSet(viewsets.ViewSet):

    @rest_login_is_required()
    def list(self, request):
        if request.user.is_staff:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.connected_with_user(user_id=request.user.id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    @rest_login_is_required()
    def retrieve(self, request, pk=None):
        if request.user.is_staff:
            queryset = Order.objects.all()
            order = get_object_or_404(queryset, pk=pk)
        else:
            queryset = Order.objects.connected_with_user(user_id=request.user.id, order_id=pk)
            if len(queryset) > 0:
                order = queryset[0]
            else:
                return Response({"status": "error", "data": None, "message": None},
                                status=status.HTTP_403_FORBIDDEN)

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    @rest_login_is_required(staff_required=True)
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = Order(**request.data)
            order.save()
            serializer = OrderSerializer(order)
            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def update(self, request, pk=None):
        order = get_object_or_404(Order.objects.all(), pk=pk)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            Order.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": serializer.data, "message": None})
        return Response({"status": "error", "errors": serializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def partial_update(self, request, pk=None):
        order = get_object_or_404(Order.objects.all(), pk=pk)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            Order.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": serializer.data, "message": None})
        return Response({"status": "error", "errors": serializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def destroy(self, request, pk=None):
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order.delete()
        return Response({"status": "success", "data": None, "message": None})
