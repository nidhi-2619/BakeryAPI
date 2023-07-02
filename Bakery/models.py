from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BakeryItem(models.Model):
    """Model representing a bakery item."""

    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='BakeryItemIngredient')
    costPrice = models.DecimalField(max_digits=8, decimal_places=2)
    sellingPrice = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class BakeryItemIngredient(models.Model):
    """Model representing the ingredients used in a bakery item."""

    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.bakery_item} - {self.ingredient}'


class Product(models.Model):
    """Model representing a product available in bakery."""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

# @login_required
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer} - {self.pk}'


class OrderItem(models.Model):
    """Model representing the items in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()