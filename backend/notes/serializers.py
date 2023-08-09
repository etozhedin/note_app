from rest_framework import serializers
from .models import Note
# from django.contrib.auth.models import User 
from users.models import User

class NoteSerializer(serializers.ModelSerializer):
      owner = serializers.ReadOnlyField(source='owner.username')
      class Meta: 
            model = Note
            fields = [
                  'pk',
                  'owner',
                  'title',
                  'content',
                  'created',
                  'updated',
            ]

class UserSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True)
      class Meta:
            model = User
            fields = (
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name'
            )
      def create(self, validated_data):
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
            return user