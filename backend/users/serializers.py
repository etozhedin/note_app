from rest_framework import serializers
# from django.contrib.auth.models import User
from django.conf import settings
from .models import User
from firebase_admin import storage


import base64
from django.core.files.base import ContentFile

# User = settings.AUTH_USER_MODEL
class UserSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True)     
      avatar = serializers.ImageField(write_only=True, required = False)  # Поле для загрузки аватара
      class Meta:
            model = User
            fields = (
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'avatar', 
                  # 'avatar_url'
            )
      def create(self, validated_data):
            avatar_data = validated_data.pop('avatar', None)
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            avatar_url = validated_data.pop('avatar_url', '')
        )
            if avatar_data:
                  avatar_data = base64.b64decode(avatar_data)
                  avatar_name = f"avatar_{user.id}.png"
                  content = ContentFile(avatar_data, name = avatar_name)

                  bucket = storage.bucket()
                  blob = bucket.blob(f"avatars/{user.id}/{avatar_name}")
                  # blob.upload_from_string(avatar_data.read(), content_type=avatar_data.content_type)
                  blob.upload_from_string(content, content_type=avatar_data.content_type)
                  # Получить URL аватарки и сохранить его в модель пользователя
                  user.avatar_url = blob.public_url
                  user.save()
                  
      
            return user
      
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar_url'
        )