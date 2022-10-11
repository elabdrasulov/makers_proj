import datetime
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

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

    filterset_fields = ['staff_position', 'direction', 'name', 'last_name']
    search_fields = ['staff_position', 'direction', 'name', 'last_name']
    ordering_fields = ['staff_position', 'direction', 'name', 'last_name']

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

@api_view(["GET"])
def ready_to_be_mentor(request):
    """
    Советует сотрудников, кто может стать ментором
    Если с начала его трекерства прошел уже год и больше, то выводится список
    """
    today = datetime.date.today()
    queryset = Staff.objects.all()
    length = len(queryset)
    objs = []
    for i in range(1,length+1):
        obj = Staff.objects.get(id=i)
        objs.append(obj)

    name = Staff._meta.get_field('name')
    last_name = Staff._meta.get_field('last_name')
    start_date = Staff._meta.get_field('trackering_start_date')
    # end_date = Staff._meta.get_field('trackering_end_date')
    staffs = {}
    allowed_staffs = []
    for obj in objs:
        date = start_date.value_from_object(obj)
        # trackering_end_date = end_date.value_from_object(obj)
        staff_name = name.value_from_object(obj)
        staff_last_name = last_name.value_from_object(obj)
        staffs[f"{staff_name} {staff_last_name}"] = date
        experience = (today - staffs.get(f"{staff_name} {staff_last_name}")).days
        if experience >= 365:
            allowed_staffs.append(
                f"{staff_name} {staff_last_name} отработал уже год! ЕБАНУТЬСЯ!"
            )

    # print(trackering_end_date)
    return Response(allowed_staffs)

