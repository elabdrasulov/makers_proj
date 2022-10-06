from django.db import models

from apps.staff.models import Staff
from django.core.validators import MaxValueValidator, MinValueValidator



class Group(models.Model):
    STUDYING_TIME = (
        ('day', 'дневная'),
        ('evening', 'вечерняя')
    )
    
    # количество студентов
    amount = models.IntegerField(default=1,validators=[MaxValueValidator(36),MinValueValidator(1)])
    # название группы
    name_of_group = models.CharField(max_length=50)
    # дата начало и конца
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    # выбор учебного времени
    group_studying_time = models.CharField(
        choices = STUDYING_TIME,
        max_length=20)
    # ментор группы
    mentor = models.ManyToManyField(
        Staff, related_name='groups'
    )
    # трекеры группы
    tracker = models.ManyToManyField(
        Staff, related_name='trackers'
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"{self.name_of_group} {self.group_studying_time} -> {self.mentor}"
