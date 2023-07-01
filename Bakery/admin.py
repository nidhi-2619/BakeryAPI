from django.contrib import admin
from .models import Ingredient, BakeryItem, BakeryItemIngredient, Product, Order, OrderItem
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(BakeryItem)
admin.site.register(BakeryItemIngredient)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)


