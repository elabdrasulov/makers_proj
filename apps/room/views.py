from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.decorators import api_view, action
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from apps.group.models import Group
from apps.group.serializers import GroupSerializer
from .models import Room
from .serializers import RoomSerializer, RoomChangeSer

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser,]

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser,]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = ['room_number']
    search_fields = ['room_number']
    ordering_fields = ['room_number']

class RoomDetailAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser,]

class RoomUpdateAPIView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser,]

class RoomDeleteAPIView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser,]

@api_view(['POST'])
def add_to_trade(request):
    serializer = RoomChangeSer(data = request.POST)
    if serializer.is_valid(raise_exception=True, ):
        return Response("successfully traded", 200)

@api_view(['GET'])
def get_free_room_day(request):
    rooms = Room.objects.filter(room_status_day=False)
    if not rooms:
        return Response(
            "Днем свободных кабинетов нет!"
        )
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_free_room_evening(request):
    rooms = Room.objects.filter(room_status_evening=False)
    if not rooms:
        return Response(
            "Вечером свободных кабинетов нет!"
        )
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)
