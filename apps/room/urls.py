from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/listing/', RoomListAPIView.as_view()),
    path('rooms/detail/<int:pk>/', RoomDetailAPIView.as_view()),
    path('rooms/delete/<int:pk>/', RoomDeleteAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomUpdateAPIView.as_view()),
    path('rooms/change_group/', add_to_trade)
]