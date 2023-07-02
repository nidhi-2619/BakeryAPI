from rest_framework import viewsets
from .models import UserRegister, UserLogin
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginViewSet(viewsets.ViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer

