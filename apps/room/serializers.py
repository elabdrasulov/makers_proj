from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.group.models import Group
from .models import Room
from .models import Room
from apps.group.models import Group
from apps.group.serializers import GroupSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # day_groups = Group.objects.filter(group_studying_time='day', id=instance.id)
        # if get_object_or_404(Room, id=instance.id).groups_room.exists():
        #     rep['day group'] = GroupSerializer(day_groups, many=True).data
        
        rep['day group'] = GroupSerializer(
            instance.groups_room.filter(group_studying_time='day'), many=True
        ).data
        rep['evening group'] = GroupSerializer(
            instance.groups_room.filter(group_studying_time='evening'), many=True
        ).data

        return rep

class RoomChangeSer(serializers.Serializer):
    room1 = serializers.IntegerField()
    room2 = serializers.IntegerField()
    group1 = serializers.CharField()
    group2 = serializers.CharField()

    
    def validate(self, attrs):
        room1 = get_object_or_404(Room, room_number = attrs.get('room1'))
        room2 = get_object_or_404(Room, room_number = attrs.get('room2'))
        group1 = get_object_or_404(Group, name_of_group = attrs.get('group1'))
        group2 = get_object_or_404(Group, name_of_group = attrs.get('group2'))

        
        if group1.amount>room1.capacity and group2.amount>room2.capacity:
            raise serializers.DjangoValidationError("нет ... нет,нет,нет так не пойдет там посмотри на вмещаемость еблан")
        elif room1.group == group1 and room2.group == group2:
            room1.group = group2
            room2.group = group1
            room1.save()
            room2.save()
        else:
            raise serializers.ValidationError("братан ты не тот человек которого я ожидал увидеть")
        


        return {}

