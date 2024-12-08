from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:pk>/', views.room, name='room'),
    path('rooms/', views.rooms, name='rooms'),
    path('create-room/', views.create_room, name='create-room'),
]