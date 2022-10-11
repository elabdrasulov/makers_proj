from random import choices
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.room.models import Room


from apps.staff.models import Staff
from django.core.validators import MaxValueValidator, MinValueValidator




class Group(models.Model):
    STUDYING_TIME = (
        ('day', 'day'),
        ('evening', 'evening')
    )
    DATE_PROMIS = (
        # (f'{}')
    )
    # количество студентов
    # amount = models.IntegerField(default=1,validators=[MaxValueValidator(36),MinValueValidator(1)])
    # название группы
    name_of_group = models.CharField(max_length=50)
    date_of_start = models.DateField(choices =  DATE_PROMIS,blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    group_studying_time = models.CharField(choices=STUDYING_TIME, max_length=20)
    number_of_students = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(36)
        ]
    )
    mentor = models.ForeignKey(
        Staff, related_name='groups_mentor', 
        on_delete=models.SET_DEFAULT, 
        default="Ментор пока не определен"
    )
    # трекеры группы
    tracker = models.ManyToManyField(
        Staff, related_name='trackers',
        blank=True, null=True
    )

    room = models.ForeignKey(
        Room, related_name='groups_room',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"{self.name_of_group} {self.group_studying_time}\
             -> {self.mentor} {self.room}"
