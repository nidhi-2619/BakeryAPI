from django.urls import path, include
from .views import IngredientViewSet, BakeryItemViewSet, ProductViewSet, OrderViewSet, OrderHistoryViewSet, \
    ProductSearchViewSet
from rest_framework.routers import DefaultRouter

# from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('bakery-items', BakeryItemViewSet, basename='bakery-items')
router.register('products', ProductViewSet, basename='products-list')
router.register('orders', OrderViewSet, basename='orders')
router.register('order-history', OrderHistoryViewSet, basename='order-history')
router.register('search', ProductSearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('order-history/<int:pk>', OrderHistoryViewSet.as_view({'get': 'retrieve'}), name='order-history-detail'),

]
