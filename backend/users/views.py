from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [~IsAuthenticated]
