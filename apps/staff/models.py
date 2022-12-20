from django.db import models
# from apps.group.models import Group
from django.utils.translation import gettext_lazy as _


class Staff(models.Model):
    DIRECTIONS = (
        ('Py', 'Python'),
        ('JS', 'Javascript')
    )

    POSITIONS = (
        ('Curator', 'Куратор'),
        ('Mentor', 'Ментор'),
        ('Tracker', 'Трекер')
    )

    RANK = (
        ('Trainee', 'Trainee'),
        ('Ninja', 'Ninja'),
        ('Ronin', 'Ronin'),
        ('Samurai', 'Samurai'),
        ('Daimio', 'Daimio')
    )

    name = models.CharField(max_length=50, verbose_name=_('имя'))
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='staff/', 
        verbose_name='Фотография', 
        blank=True, null=True
    )
    direction = models.CharField(
        choices=DIRECTIONS, 
        max_length=50, 
        blank=True, 
        null=True,
        verbose_name='Направление'
    )
    staff_position = models.CharField(
        choices=POSITIONS, max_length=20, verbose_name='Должность'
    )

    staff_rank = models.CharField(
        choices=RANK, max_length=20, verbose_name='Rang',
        blank=True, null=True
    )

    # начало/конец стажировки
    start_of_training = models.DateField(
        verbose_name="Начало стажировки", blank=True, null=True
    )
    end_of_training = models.DateField(
        verbose_name="Конец стажировки", blank=True, null=True
    )
    
    # заметки о сотруднике
    notes = models.TextField(
        max_length=1000, 
        verbose_name="Дополнительно(заметки)",
        blank=True, null=True
    )

    # когда планирует уйти
    plans_to_leave = models.DateField(blank=True, null=True)

    mentor_status_day = models.BooleanField(default=False)
    mentor_status_evening = models.BooleanField(default=False)
    # старт/конец работы трекером, ментором, куратором
    trackering_start_date = models.DateField(
        verbose_name="Начало работы трекером", blank=True, null=True
    )
    trackering_end_date = models.DateField(
        verbose_name="Конец работы трекером", blank=True, null=True
    )
    
    mentoring_start_date = models.DateField(
        verbose_name="Начало работы ментором", blank=True, null=True
    )
    mentoring_end_date = models.DateField(
        verbose_name="Конец работы ментором", blank=True, null=True
    )
    
    curatoring_start_date = models.DateField(
        verbose_name="Начало работы куратором", blank=True, null=True
    )
    curatoring_end_date = models.DateField(
        verbose_name="Конец работы куратором", blank=True, null=True
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.name} {self.last_name} -> {self.staff_position}"
