from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Group
from apps.staff.serializers import StaffSerializer

class GroupSerializer(
    WritableNestedModelSerializer,
    serializers.ModelSerializer
):
    mentor = StaffSerializer()

    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.room:
            rep['room'] = instance.room.room_number
        rep['tracker'] = StaffSerializer(instance.tracker.all(), many=True).data
        return rep
