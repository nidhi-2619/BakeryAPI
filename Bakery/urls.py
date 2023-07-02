from django.urls import path, include
from .views import IngredientViewSet,BakeryItemViewSet,ProductListViewSet,OrderViewSet,OrderHistoryViewSet,ProductSearchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('bakery-items', BakeryItemViewSet, basename='bakery-items')
router.register('', ProductListViewSet, basename='products')
router.register('products', ProductListViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('order-history', OrderHistoryViewSet, basename='order-history')
router.register('search', ProductSearchViewSet, basename='search')


urlpatterns = [
    path('', include(router.urls)),
    path('/orders/<int:pk>', OrderViewSet.as_view({'get': 'retrieve'}), name='order-detail'),
    path('/order-history/<int:pk>', OrderHistoryViewSet.as_view({'get': 'retrieve'}), name='order-history-detail'),

]