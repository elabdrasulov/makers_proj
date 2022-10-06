from rest_framework import serializers
from .models import Group
from apps.staff.serializers import StaffSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['mentor'] = f"{instance.mentor.name} {instance.mentor.last_name}"
        if instance.room:
            rep['room'] = instance.room.room_number
        rep['tracker'] = StaffSerializer(instance.tracker.all(), many=True).data
        return rep
