from django.urls import path
from .views import CustomerRegistrationAPIView,PlaceOrderAPIView, OrderHistoryAPIView

urlpatterns = [
    path('customers/register/', CustomerRegistrationAPIView.as_view(), name='customer-register'),
    path('orders/place/', PlaceOrderAPIView.as_view(), name='place-order'),
    path('orders/history/', OrderHistoryAPIView.as_view(), name='order-history'),
]