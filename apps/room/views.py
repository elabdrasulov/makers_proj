from .serializers import RoomSerializer
from .models import Room
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from .serializers import RoomChangeSer
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer


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