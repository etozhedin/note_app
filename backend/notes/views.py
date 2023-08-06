from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Note
from .serializers import NoteSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from api.permissions import isOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class NoteListAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]    
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]
    def get_queryset(self):
        queryset= Note.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content')
        created = serializer.validated_data.get('created')
        owner = self.request.user
        if created is None:
            created = datetime.now()

        serializer.save(created = created, owner = owner)
note_list_create_view = NoteListAPIView.as_view()

class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]
note_retrieve_update_destroy_view = NoteRetrieveUpdateDestroy.as_view()

class NoteListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer