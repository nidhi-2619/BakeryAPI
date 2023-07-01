from django.urls import path
from .views import IngredientAPIView, BakeryItemAPIView, ProductListAPIView, ProductSearchAPIView

urlpatterns = [
    path('ingredients/', IngredientAPIView.as_view(), name='ingredients'),
    path('', BakeryItemAPIView.as_view(), name='bakery-items'),
    path('bakery-items/<int:bakery_item_id>/', BakeryItemAPIView.as_view(), name='bakery-item'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/search/', ProductSearchAPIView.as_view(), name='product-search'),
]