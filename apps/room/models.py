from django.db import models

from apps.staff.models import Staff
from apps.group.models import Group

class Room(models.Model):
    room_name = models.IntegerField()
    capacity = models.IntegerField()
    room_status = models.BooleanField(default=False)
    mentor = models.ForeignKey(
        Staff, related_name='rooms', 
        on_delete=models.SET_DEFAULT,
        default='кабинет свободен'
    )
    group = models.ForeignKey(Group, related_name='rooms', on_delete=models.CASCADE)
