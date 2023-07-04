from django.contrib.auth.decorators import login_required
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(auto_created=True, default=0)

    def __str__(self):
        return self.name

class InventoryIngredient(models.Model):
    """Model representing the inventory of an ingredient."""

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(auto_created=True, default=0)

    def __str__(self):
        return f'{self.ingredient} - {self.quantity}'

class BakeryItem(models.Model):
    """Model representing a bakery item."""

    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient,through='BakeryItemDetails')

    def __str__(self):
        return self.name


class InventoryBakeryItem(models.Model):
    """Model representing the inventory of a bakery item."""

    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(auto_created=True, default=0)

    def __str__(self):
        return f'{self.bakery_item} - {self.quantity}'


class BakeryItemDetails(models.Model):
    """Model representing the ingredients used in a bakery item."""
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='ingredient')
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'Item Name: {self.bakery_item} |  Ingredients (%): {self.ingredient} | Cost Price: {self.cost_price} | Selling Price: {self.selling_price}'


class Product(models.Model):
    """Model representing a product available in bakery."""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_available = models.PositiveIntegerField(auto_created=True, default=0)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.quantity_available}'


class OrderItem(models.Model):
    """Model representing the items in an order."""
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.order} - {self.product} - {self.quantity}'

