from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('rooms', (RoomViewSet))

urlpatterns = [
    # path('', include(router.urls)),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomUpdateAPIView.as_view()),
    path('rooms/change_group/', add_to_trade),
    path('rooms/get_free_room/', get_free_room),
    # path('rooms/get_analyz/', get_analyz_of_room),
    # path('rooms/test/', test),
    path('rooms/delete/<int:pk>/', RoomDeleteAPIView.as_view()),
]