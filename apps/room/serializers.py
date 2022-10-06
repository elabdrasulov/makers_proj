from django.shortcuts import get_object_or_404
from rest_framework import serializers

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