from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Note
from .serializers import NoteSerializer
from datetime import datetime

class NoteListAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content')
        created = serializer.validated_data.get('created')
        if created is None:
            created = datetime.now()
        serializer.save(created = created)
note_list_create_view = NoteListAPIView.as_view()

class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
 
note_retrieve_update_destroy_view = NoteRetrieveUpdateDestroy.as_view()