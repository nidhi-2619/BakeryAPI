from rest_framework.views import APIView
from .models import UserRegister, UserLogin
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user_register = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user_login = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

