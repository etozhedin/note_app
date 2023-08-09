from django.urls import path
from .views import UserRegistration, UserDetailView
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_registration'),
    path('detail/', UserDetailView.as_view(), name = 'user_detail')
]
