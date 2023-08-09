from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import isOwnerOrReadOnly
from .models import User
# Create your views here.
class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [~IsAuthenticated]


class UserDetailView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, isOwnerOrReadOnly)
    def get_queryset(self):
        queryset = User.objects.all().filter(username = self.request.user)
        return queryset
    def perform_create(self, serializer):
        avatar_url = serializer.validated_data.get('avatar_url')
        serializer.save(avatar_url = avatar_url)