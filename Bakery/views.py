from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product, Order, OrderItem
from .serializers import IngredientSerializer, BakeryItemSerializer, ProductListSerializer, OrderSerializer, OrderItemSerializer, ProductSearchSerializer
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

    queryset = Product.objects.get_queryset()
    serializer_class = ProductListSerializer

class ProductSearchViewSet(viewsets.ModelViewSet):
    """View for searching a product."""
    def get(self, request, format=None, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSearchSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    """View for creating a new order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderHistoryViewSet(viewsets.ModelViewSet):
    """View for viewing order history."""
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class PlaceOrderViewSet(viewsets.ModelViewSet):
    """View for placing a new order."""
    permission_classes = [IsAuthenticated]
    def create(self, request):
        items_data = request.data.pop('items')
        order = Order.objects.create(customer=request.user)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return Response("Order Placed Successfully")
