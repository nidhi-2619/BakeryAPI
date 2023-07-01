# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.customer} - {self.pk}'
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()