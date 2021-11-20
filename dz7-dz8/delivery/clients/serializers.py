from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'status', 'home_address', 'user']


class ClientUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    home_address = serializers.IntegerField()
    user = serializers.IntegerField()

    def validate(self, data):
        user = data['user']
        errors = {}
        if Client.objects.filter(user=user).exclude(id=data['id']).exists():
            errors['user'] = 'User id is not unique'
            raise ValidationError(errors)
        return data
