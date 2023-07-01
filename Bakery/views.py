from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product
from .serializers import IngredientSerializer, BakeryItemSerializer, ProductSerializer
# Create your views here.
class IngredientAPIView(APIView):
    """View for creating a new ingredient."""
    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

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