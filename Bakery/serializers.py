from rest_framework import serializers
from .models import Ingredient, BakeryItem, BakeryItemDetails, Product, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class PlaceOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['items', 'quantity']
class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BakeryItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItemDetails
        fields = '__all__'

class BakeryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItem
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    # def post(self):
    #     user = self.context['request'].user
    #     product = Product.objects.create(user=user, **self.validated_data)

    class Meta:
        model = Product
        fields = ['name','price']

class ProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name','price']


