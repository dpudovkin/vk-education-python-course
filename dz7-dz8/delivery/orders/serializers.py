from rest_framework import serializers

from orders.models import Order, Address


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id",'destination_client', 'arriving_client', 'destination_address',
                  'arriving_address', 'cost', 'comment', 'status', 'base_award', 'performer']

    def create(self, validated_data):
        data = {
            'destination_client_id': validated_data['destination_client'],
            'arriving_client_id': validated_data['arriving_client'],
            'destination_address_id': validated_data['destination_address'],
            'arriving_address_id': validated_data['arriving_address'],
            'cost': validated_data['cost'],
            'comment': validated_data['comment'],
            'status': validated_data['status'],
            'base_award': validated_data['base_award'],
            'performer_id': validated_data['performer'],
        }
        return Order.objects.create(**data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id","full_name", "longitude", "latitude"]
