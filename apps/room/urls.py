from django.urls import path, include
from .views import *

urlpatterns = [
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomUpdateAPIView.as_view()),
    path('rooms/change_group/', add_to_trade),
    path('rooms/free/day/', get_free_room_day),
    path('rooms/free/evening/', get_free_room_evening),
    # path('rooms/get_analyz/', get_analyz_of_room),
    # path('rooms/test/', test),
    path('rooms/delete/<int:pk>/', RoomDeleteAPIView.as_view()),
]