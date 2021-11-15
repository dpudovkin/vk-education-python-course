from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from clients.models import Client
from clients.serializers import ClientSerializer, ClientUpdateSerializer


class ClientViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        client = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = Client(request.data)
            client.save()
            serializer = ClientSerializer(client)
            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        updateSerializer = ClientUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Client.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        updateSerializer = ClientUpdateSerializer(data=request.data)
        if updateSerializer.is_valid():
            Client.objects.filter(pk=pk).update(**self.request.data)
            return Response({"status": "success", "data": updateSerializer.data, "message": None})
        return Response({"status": "error", "errors": updateSerializer.errors, "message": None},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response({"status": "success", "data": None, "message": None})
