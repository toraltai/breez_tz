from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['customer', 'total']

    customer = serializers.CharField(read_only=True)
    total = serializers.IntegerField()