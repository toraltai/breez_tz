from rest_framework import serializers
from .models import Product, Customer


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
    

class CustomerSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(read_only=True)
    total = serializers.SerializerMethodField()
    item = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def get_total(self, obj):
        total = sum(product.total for product in obj.products.all())
        return total