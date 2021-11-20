from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from application.views import rest_login_is_required
from clients.models import Client
from clients.serializers import ClientSerializer, ClientUpdateSerializer


class ClientViewSet(viewsets.ViewSet):

    @rest_login_is_required()
    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @rest_login_is_required()
    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        client = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @rest_login_is_required(staff_required=True)
    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.create(validated_data=request.data)
            # client = Client(**request.data)
            # client.save()
            serializer = ClientSerializer(client)
            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def update(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        updateSerializer = ClientUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Client.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def partial_update(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        updateSerializer = ClientUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Client.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    @rest_login_is_required(staff_required=True)
    def destroy(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response({"status": "success", "data": None, "message": None})
