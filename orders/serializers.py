from rest_framework import serializers

from orders.models import Order, Order_product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields = '__all__'
