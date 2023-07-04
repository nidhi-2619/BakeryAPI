from django.contrib import admin
from .models import Ingredient, BakeryItem, BakeryItemDetails, Product,OrderItem
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(BakeryItem)
admin.site.register(BakeryItemDetails)
admin.site.register(Product)
admin.site.register(OrderItem)


