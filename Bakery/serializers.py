from rest_framework import serializers
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product
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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'