from rest_framework import serializers

from orders.models import Order, Address


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['destination_client', 'arriving_client', 'destination_address',
                  'arriving_address', 'cost', 'comment', 'status', 'base_award', 'performer']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["full_name", "longitude", "latitude"]
