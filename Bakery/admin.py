from django.contrib import admin
from .models import Ingredient, BakeryItem, Product,OrderItem
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(BakeryItem)
admin.site.register(Product)
admin.site.register(OrderItem)

# def Login(Authentication):
#     post_data = {'username': 'admin', 'password': 'admin'}

