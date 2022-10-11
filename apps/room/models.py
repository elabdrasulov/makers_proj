from django.db import models
# from apps.group.models import Group

# from apps.staff.models import Staff
# from apps.group.models import Group

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
    
    def __str__(self) -> str:
        return f'{self.room_number} {self.capacity}'