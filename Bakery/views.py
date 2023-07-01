from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
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

class BakeryItemAPIView(APIView):
    """View for creating a new bakery item."""
    def post(self, request):
        serializer = BakeryItemSerializer(data=request.data)
        if serializer.is_valid():
            bakery_item = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, bakery_item):
        try:
            bakery_item = BakeryItem.objects.get(name=bakery_item)
            serializer = BakeryItemSerializer(bakery_item)
            return Response(serializer.data)
        except BakeryItem.DoesNotExist:
            return Response({'message': 'BakeryItem not found'}, status=404)


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductSearchAPIView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q')
        products = Product.objects.filter(name__icontains=search_query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CustomerRegistrationAPIView(APIView):
    """View for registering a new customer."""
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'message': 'Username, password, and email are required.'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'Registration successful.'}, status=201)


class OrderHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.create(customer=request.user)
        for item_data in request.data.get('items', []):
            product = Product.objects.get(pk=item_data['product_id'])
            quantity = item_data['quantity']
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
        bill = order.calculate_bill()
        return Response({'message': 'Order placed successfully.', 'bill': bill}, status=201)

