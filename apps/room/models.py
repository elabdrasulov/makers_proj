from email.policy import default
from django.db import models
# from apps.group.models import Group

from apps.staff.models import Staff

class Room(models.Model):
    room_number = models.IntegerField()
    
    # Вместимость кабинета
    capacity = models.IntegerField()
    
    # Свободен ли кабинет
    room_status_day = models.BooleanField(default=False)
    room_status_evening = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        return f"Кабинет №{self.room_number} -> вместимость {self.capacity}"