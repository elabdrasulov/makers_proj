from django.db import models

from apps.staff.models import Staff

class Group(models.Model):
    STUDYING_TIME = (
        ('day', 'дневная'),
        ('evening', 'вечерняя')
    )
    name_of_group = models.CharField(max_length=50)
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    group_studying_time = models.CharField(max_length=20)
    mentor = models.ManyToManyField(
        Staff, related_name='groups'
    )
    tracker = models.ManyToManyField(
        Staff, related_name='trackers'
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"{self.name_of_group} {self.group_studying_time} -> {self.mentor}"
