from django.urls import path, include
from .views import IngredientViewSet, BakeryItemViewSet, ProductViewSet, OrderViewSet, OrderHistoryViewSet, \
    ProductSearchViewSet


urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('', ProductViewSet.as_view({'get': 'list'}), name='products'),
    path('order-history/<int:pk>', OrderHistoryViewSet.as_view({'get': 'retrieve'}), name='order-history-detail'),
    path('products/', ProductViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='products-detail'),
    path('bakery-items/', BakeryItemViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='bakery-items'),
    path('bakery-items/<int:pk>', BakeryItemViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='bakery-items-detail'),
    path('ingredients/<int:pk>', IngredientViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='ingredients-detail'),
    path('search/', ProductSearchViewSet.as_view({'get':'retrieve'}), name='search'),
    path('orders/', OrderViewSet.as_view({'get':'retrieve'}), name='orders'),

]
