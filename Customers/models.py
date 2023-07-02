from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.email}'

class UserLogin(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email} - {self.password}'


