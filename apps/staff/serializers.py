from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.BaseSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
