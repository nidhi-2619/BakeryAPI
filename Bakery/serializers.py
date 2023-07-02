from rest_framework import serializers
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BakeryItemIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = BakeryItemIngredient
        fields = ('ingredient', 'quantity_percentage')

class BakeryItemSerializer(serializers.ModelSerializer):
    ingredients = BakeryItemIngredientSerializer(many=True)

    class Meta:
        model = BakeryItem
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price']

class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price']
