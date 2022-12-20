import datetime
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Group
from apps.room.models import Room
from apps.staff.models import Staff
from .serializers import GroupSerializer
from .tasks import graduate_group

from config.settings import TIME_ZONE


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

    def post(self, request):
        room_id = request.data.get('room')
        Group.DATE_PROMIS = (
            ('2022-10-10','2022-10-10'),
            )
        
        name = request.data.get('name_of_group')
        start_date = request.data.get('date_of_start')
        end_date = request.data.get('date_of_end')
        time = request.data.get('group_studying_time')
        mentor_id = request.data.get('mentor')
        tracker_id = request.data.get('tracker')
        students = request.data.get('number_of_students')
        
        if int(students)>36:
            return Response("В группе не может быть больше 36 студентов!", 400)
        
        # print("room", room_id, Room.objects.all())
        room = get_object_or_404(Room, id=room_id)
        # print("mentor", mentor_id, Staff.objects.all())
        mentor = get_object_or_404(Staff, id=mentor_id)
        # print(mentor)

        if room.groups_room.exists() and room.room_status_day == True and time=='day':
            return Response('Кабинет днем занят!', 400)
        elif room.groups_room.exists() and room.room_status_evening == True and time=='evening':
            return Response('Кабинет вечером занят!', 400)

        if mentor.groups_mentor.exists() and mentor.mentor_status_day == True:
            return Response('Ментор занят днем долбоеб', 400)
        elif mentor.groups_mentor.exists() and mentor.mentor_status_evening == True:
            return Response('Ментор занят вечером долбоеб', 400)

        group = Group.objects.create(
            name_of_group=name,
            date_of_start=start_date,
            date_of_end=end_date,
            group_studying_time=time,
            mentor=mentor,
            number_of_students=students,
            room=room,
        )
        if type(tracker_id) == list:
            for t_id in tracker_id:
                group.tracker.add(t_id)
        elif type(tracker_id) == str:
            for t_id in tracker_id.split(','):
                group.tracker.add(t_id)
        else:
            group.tracker.add(tracker_id)
        
        if room is not None and time=='day':
            room.room_status_day = True
            room.save()
        elif room is not None and time=='evening':
            room.room_status_evening = True
            room.save()
        serializer = GroupSerializer(group)

        if mentor.mentor_status_day is not None and time=='day':
            mentor.mentor_status_day = True
            mentor.save()
        elif mentor.mentor_status_evening is not None and time=='evening':
            mentor.mentor_status_evening = True
            mentor.save()

        return Response(serializer.data)
        
        


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = ['name_of_group', 'group_studying_time']
    search_fields = ['name_of_group', 'group_studying_time']
    ordering_fields = ['number_of_students']

class GroupDetailAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

class GroupUpdateAPIView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.room.groups_room.exists() and instance.room.room_status_day == True and request.data['group_studying_time']=='day':
            return Response('Кабинет днем занят!', 400)
        elif instance.room.groups_room.exists() and instance.room.room_status_evening == True and request.data['group_studying_time']=='evening':
            return Response('Кабинет вечером занят!', 400)
        try:
            time = request.data['group_studying_time']
            if time == 'day' or time == 'evening':
                return Response('Нельзя изменить время обучения!', 400)
        except:
            pass

        try: 
            room_id = request.data['room']
            room = get_object_or_404(Room, id=room_id)

            if instance.number_of_students > room.capacity:
                return Response(
                    f'Студентов больше, чем вместимость({room.capacity}) кабинета!', 400
                )
            
            if instance.group_studying_time=='day':
                room.room_status_day = True
                room.save()
                if instance.room:
                    instance.room.room_status_day = False
                    instance.room.save()
            elif instance.group_studying_time=='evening':
                room.room_status_evening = True
                room.save()
                if instance.room:
                    instance.room.room_status_evening = False
                    instance.room.save()
            
        except:
            pass
        
        # if instance.room.groups_room.exists() and instance.room.room_status_day == True and request.data['group_studying_time']=='day':
        #     return Response('Дневная группа занята', 400)
        # elif instance.room.groups_room.exists() and instance.room.room_status_evening == True and request.data['group_studying_time']=='evening':
        #     return Response('Вечерняя группа занята', 400)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if request.data['group_studying_time']=='day':
            instance.room_status_day = True
            instance.save()
        elif request.data['group_studying_time']=='evening':
            instance.room_status_evening = True
            instance.save()
        # if getattr(instance, '_prefetched_objects_cache', None):
        #     instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()

        try:
            time = request.data['group_studying_time']
            if time == 'day' or time == 'evening':
                return Response('Нельзя изменить время обучения!', 400)
        except:
            pass

        try: 
            room_id = request.data['room']
            room = get_object_or_404(Room, id=room_id)

            if instance.number_of_students > room.capacity:
                return Response(
                    f'Студентов больше, чем вместимость({room.capacity}) кабинета!', 400
                )

            if instance.group_studying_time=='day':
                room.room_status_day = True
                room.save()
                if instance.room:
                    instance.room.room_status_day = False
                    instance.room.save()
            elif instance.group_studying_time=='evening':
                room.room_status_evening = True
                room.save()
                if instance.room:
                    instance.room.room_status_evening = False
                    instance.room.save()
        except:
            pass

        return super().put(request, *args, **kwargs)



class GroupDeleteAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            'Группа была успешно удалена!', status=status.HTTP_204_NO_CONTENT
        )

    def perform_destroy(self, instance):
        instance.delete()
        if instance.group_studying_time == 'day':
            instance.room.room_status_day = False
            instance.room.save()
        elif instance.group_studying_time == 'evening':
            instance.room.room_status_evening == False
            instance.room.save()


@api_view(['GET'])
def graduate_group(request):
    # groups = Group.objects.all()
    # today = datetime.date.today()
    # graduated_groups = []
    # for group in groups:
    #     name = f"выпустилась {group.name_of_group} в {today}"
    #     if group.date_of_end:
    #         if group.date_of_end == today:
    #             graduated_groups.append(name)
    #             group.is_graduated = True
    #             group.save()
            
    # return Response(graduated_groups)
    graduate_group.delay()

@api_view(['GET'])
def queue(request, r_id):
    group_id = request.data
    room = get_object_or_404(Room, id=r_id)

    # if room.room_status_day

    return Response('ok')
