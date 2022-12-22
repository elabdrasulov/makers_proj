import datetime
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from apps.group.models import Group

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

@api_view(["GET"])
def free_mentor(request):
    """
    если ментор свободен или до окончания его группы осталось <int> дней,
    то он предлагается как свободный
    """
    day_mentors = []
    evening_mentors = []
    groups = Group.objects.all()
    mentors = Staff.objects.all()

    for mentor in mentors:
        if not mentor.mentor_status_day:
            day_mentors.append(StaffSerializer(mentor).data)
            # mentor_info = f"{mentor.name} {mentor.last_name} {mentor.staff_position}(без дневной группы)"
            # if mentor.plans_to_leave:
            #     mentor_info += f" планирует уйти с мейкерс {mentor.plans_to_leave}"
            # else:
            #     mentor_info += f" не указана дата ухода"
            # day_mentors.append(mentor_info)
        if not mentor.mentor_status_evening:
            evening_mentors.append(StaffSerializer(mentor).data)
            # mentor_info = f"{mentor.name} {mentor.last_name} {mentor.staff_position}(без вечерней группы)"
            # if mentor.plans_to_leave:
            #     mentor_info += f" планирует уйти с мейкерс {mentor.plans_to_leave}"
            # else:
            #     mentor_info += f" не указана дата ухода"
            # evening_mentors.append(mentor_info)

    res = []

    for group in groups:
        if group.mentor.groups_mentor.exists() and group.is_graduated == False:
            if group.date_of_end:
                today = datetime.date.today()
                end_date = group.date_of_end
                days = (end_date - today).days
                
                if days<30:
                    who_mentor = {
                        'mentor': StaffSerializer(group.mentor).data,
                        'days_until_the_end': days

                    }
                    res.append(who_mentor)

                    for tracker in group.tracker.all():
                        who_tracker = {
                            'tracker': StaffSerializer(tracker).data,
                            'days_until_the_end': days
                        }
                        res.append(who_tracker)

                # if group.mentor.plans_to_leave:
                #     plans_to_leave = group.mentor.plans_to_leave
                #     mentor_info = f"{group.mentor.name} {group.mentor.last_name} - {group.mentor.staff_position}, {plans_to_leave}"
                # else:
                #     mentor_info = f"{group.mentor.name} {group.mentor.last_name} - {group.mentor.staff_position}, у ментора не указана дата ухода"
                
                # trackers = []

                # for tracker in group.tracker.all():
                #     if tracker.plans_to_leave:
                #         plans_to_leave = tracker.plans_to_leave
                #         tracker_info = f"{tracker.name} {tracker.last_name} - {tracker.staff_position}, {plans_to_leave}"
                #         trackers.append(tracker_info)
                #     else:
                #         tracker_info = f"{tracker.name} {tracker.last_name} - {tracker.staff_position}, у трекера не указана дата ухода"
                #         trackers.append(tracker_info)


                # if group.group_studying_time == 'day':
                #     studying_time = 'дневная'
                # else:
                #     studying_time = 'вечерка'


                # if days<30:

                #     who_mentor = {
                #         mentor_info: f"Группа {group.name_of_group} {studying_time} - до окончания осталось - {days} дней ({group.date_of_end})"
                #     }
                #     # res.append(who_mentor)

                #     for tracker in trackers:
                #         who_tracker = {
                #             tracker: f"Группа {group.name_of_group} {studying_time} - до окончания осталось - {days} дней ({group.date_of_end})"
                #         }
                #     # res.append(who_tracker)
                # else:
                #     fraza = f"В ближайшие 30 дней никто не освободится"
                #     res.append(fraza)

    data = {
        'isFreeDay': day_mentors,
        'isFreeEvening': evening_mentors,
        'willBeFreeSoon': res
    }
    return Response(data)
    
