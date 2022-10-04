from email.policy import default
from django.db import models

from apps.staff.models import Staff

class Room(models.Model):
    room_number = models.IntegerField()
    
    # Вместимость кабинета
    capacity = models.IntegerField()
    
    # Свободен ли кабинет
    room_status = models.BooleanField(default=False)


    mentor = models.ForeignKey(
        Staff, related_name='rooms', 
        on_delete=models.SET_DEFAULT,
        default='кабинет свободен'
    )
    # group = models.ForeignKey()

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"

    def __str__(self):
        return f"Кабинет №{self.room_number} -> вместимость {self.capacity}"