from django.urls import path, include
from .views import IngredientViewSet,BakeryItemViewSet,ProductListViewSet,OrderViewSet,OrderHistoryViewSet,ProductSearchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('bakery-items', BakeryItemViewSet, basename='bakery-items')
router.register('products', ProductListViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')


urlpatterns = [
    path('', include(router.urls)),
    path('search/', ProductSearchViewSet.as_view({'get': 'list'}), name='search'),
]