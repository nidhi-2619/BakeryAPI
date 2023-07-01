from django.urls import path, include
from .views import IngredientViewSet, BakeryItemAPIView, ProductListAPIView, ProductSearchAPIView,CustomerRegistrationAPIView,PlaceOrderAPIView, OrderHistoryAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    # path('', include(router.urls)),
    path('ingredients/', IngredientViewSet.as_view({'get': 'list', 'post': 'create'}), name='ingredients'),
    path('bakery/', BakeryItemAPIView.as_view(), name='bakery-items'),
    path('bakery-items/<int:bakery_item_id>/', BakeryItemAPIView.as_view(), name='bakery-item'),
    path('', ProductListAPIView.as_view(), name='products'),
    path('products/search/', ProductSearchAPIView.as_view(), name='product-search'),
    path('register/', CustomerRegistrationAPIView.as_view(), name='customer-register'),
    path('orders/place/', PlaceOrderAPIView.as_view(), name='place-order'),
    path('orders/history/', OrderHistoryAPIView.as_view(), name='order-history'),
]