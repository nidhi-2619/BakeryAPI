from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Ingredient, BakeryItem, BakeryItemDetails, Product, OrderItem
from .serializers import (
    IngredientSerializer, BakeryItemSerializer, ProductListSerializer, PlaceOrderSerializer,
    OrderItemSerializer, ProductSearchSerializer, OrderHistorySerializer)
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class IngredientViewSet(viewsets.ModelViewSet):
    """View for creating a new ingredient."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class BakeryItemViewSet(viewsets.ModelViewSet):
    """View for creating a new bakery item."""
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

    def post(self, request, format=None):
        serializer = BakeryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductViewSet(viewsets.ModelViewSet):
    """View for creating a new product."""

    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def post(self, request, format=None):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductSearchViewSet(viewsets.ModelViewSet):
    """View for searching a product."""
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'name', 'price', 'ingredients']

    def get(self, request, format=None, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSearchSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    """View for creating a new order."""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderHistoryViewSet(viewsets.ModelViewSet):
    """
    This view should return a list of all the purchases
    for the currently authenticated user.
    """
    # permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        queryset = OrderItem.objects.filter(customer=request.user)
        serializer = OrderHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class PlaceOrderViewSet(viewsets.ModelViewSet):
    """View for placing a new order."""
    # permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = PlaceOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'price', 'ingredients']

    def create(self, request):
        items_data = request.data.pop('items')
        order = OrderItem.objects.create(customer=request.user)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return Response("Order Placed Successfully")
