from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product, Order, OrderItem
from .serializers import IngredientSerializer, BakeryItemSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
class IngredientViewSet(viewsets.ModelViewSet):
    """View for creating a new ingredient."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class BakeryItemViewSet(viewsets.ModelViewSet):
    """View for creating a new bakery item."""
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class ProductListViewSet(viewsets.ModelViewSet):
    """View for creating a new product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSearchViewSet(viewsets.ModelViewSet):
    """View for searching a product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """View for creating a new order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderHistoryViewSet():
    permission_classes = [IsAuthenticated]


class PlaceOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
