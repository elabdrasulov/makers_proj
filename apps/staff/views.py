from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.staff.models import Staff
from apps.staff.serializers import StaffSerializer


class StaffCreateAPIView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser,]

class StaffListAPIView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser,]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = []
    search_fields = []
    ordering_fields = []

class StaffDetailAPIView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser,]

class StaffUpdateAPIView(UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser,]

class StaffDeleteAPIView(DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser,]
