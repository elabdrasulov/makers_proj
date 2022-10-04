from .serializers import RoomSerializer
from .models import Room
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser,]

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser,]

class RoomDetailAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser,]

class RoomUpdateAPIView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser,]

class RoomDeleteAPIView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser,]