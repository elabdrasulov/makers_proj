import datetime

from rest_framework import serializers

from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        today = datetime.date.today()
        if instance.trackering_start_date:
            track_exp = today - instance.trackering_start_date
            rep['tracker experience'] = f"{track_exp.days} дней"
        if instance.mentoring_start_date:
            ment_exp = today - instance.mentoring_start_date
            rep['mentoring experience'] = f"{ment_exp.days} дней"
        return rep
