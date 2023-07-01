# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from .models import Order, OrderItem, Product
# from .serializers import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
#
#
# # Create your views here.
# class CustomerRegistrationAPIView(APIView):
#     """View for registering a new customer."""
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#
#         if not username or not password or not email:
#             return Response({'message': 'Username, password, and email are required.'}, status=400)
#
#         user = User.objects.create_user(username=username, password=password, email=email)
#         return Response({'message': 'Registration successful.'}, status=201)
#
#
# class OrderHistoryAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         orders = Order.objects.filter(customer=request.user)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#
# class PlaceOrderAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         order = Order.objects.create(customer=request.user)
#         for item_data in request.data.get('items', []):
#             product = Product.objects.get(pk=item_data['product_id'])
#             quantity = item_data['quantity']
#             order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
#         bill = order.calculate_bill()
#         return Response({'message': 'Order placed successfully.', 'bill': bill}, status=201)
#
