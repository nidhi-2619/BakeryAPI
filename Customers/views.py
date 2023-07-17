from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserLogin(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [JWTAuthentication]
    serializer_class = UserLoginSerializer


