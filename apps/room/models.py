from email.policy import default
from django.db import models

from apps.staff.models import Staff

class Room(models.Model):
    capacity = models.IntegerField()
    room_status = models.BooleanField(default=False)
    mentor = models.ForeignKey(
        Staff, related_name='rooms', 
        on_delete=models.SET_DEFAULT,
        default='кабинет свободен'
    )
    # group = models.ForeignKey()

