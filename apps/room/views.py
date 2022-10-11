from apps.group.serializers import GroupSerializer
from .serializers import RoomChangeSer

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view, action
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Room
from .serializers import RoomSerializer, Analyz
from rest_framework.filters import SearchFilter
from apps.group.models import Group
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
    # filter_fields = [

    # ]

    filterset_fields = []
    search_fields = []
    ordering_fields = []

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
def get_free_room(request):
    free_room = Room.objects.all()
    free_rooms = []
    for f_r in free_room:
        if f_r.room_status_day == False or f_r.room_status_evening==False:
            f_r = RoomSerializer(f_r)
            free_rooms.append(f_r.data)
    return Response(free_rooms)

# @api_view(['POST'])
# def get_analyz_of_room(request):
#     analyz_of_group = Group.objects.all()
#     # if request.data['group_studying_time']=='day':
#     #     analyz_of_group.room_status_day = False
#     #     analyz_of_group.save()
#     # elif request.data['group_studying_time']=='evening':
#     #     analyz_of_group.room_status_evening = False
#     #     analyz_of_group.save()
#     #     # self.perform_destroy(instance=instance)
#     analyz_of_groups = []
#     for f_r in analyz_of_group:
#         # if request == f_r.date_of_end:
#             f_r = GroupSerializer(f_r)
#             return Response(f_r.data)
#     # analyz_of_group = GroupSerializer(analyz_of_group)
#     return Response("not ok")

# @api_view(["POST"])
# def test(request):
#     serializer = Analyz(data=request.POST)
#     if serializer.is_valid(raise_exception=True):
#         print(serializer)
#         return Response('success', 200)