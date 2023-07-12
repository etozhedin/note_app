from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

    # title = serializers.CharField(source = 'title')
    # content = serializers.CharField(source='content')
    # created = serializers.DateTimeField(source = 'created')
    # updated = serializers.DateTimeField(source='updated')

    class Meta: 
            model = Note
            fields = [
                  'pk',
                  'title',
                  'content',
                  'created',
                  'updated',
            ]