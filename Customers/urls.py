from django.urls import path, include
from .views import UserRegisterViewSet, UserLoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', UserRegisterViewSet, basename='register')
router.register('login', UserLoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),

]