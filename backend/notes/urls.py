from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list_create_view),
    path('<int:pk>/', views.note_retrieve_update_destroy_view, name='note-detail'),
    # path('<int:pk>/update/', views.note_retrieve_update_destroy_view, name='note-update'),
    # path('<int:pk>/delete/', views.note_retrieve_update_destroy_view, name='note-delete'),
]