from django.db import models


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

    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
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
    staff_position = models.CharField(choices=POSITIONS, max_length=20, verbose_name='Должность')

    # начало/конец стажировки
    start_of_training = models.DateField(
        verbose_name="Начало стажировки", blank=True, null=True
    )
    end_of_training = models.DateField(
        verbose_name="Конец стажировки", blank=True, null=True
    )
    
    # старт/конец работы трекером, ментором, куратором
    trackering_start_date = models.DateField(
        verbose_name="Начало работы трекером", blank=True
    )
    trackering_end_date = models.DateField(
        verbose_name="Конец работы трекером", blank=True
    )
    
    mentoring_start_date = models.DateField(
        verbose_name="Начало работы ментором", blank=True
    )
    mentoring_end_date = models.DateField(
        verbose_name="Конец работы ментором", blank=True
    )
    
    curatoring_start_date = models.DateField(
        verbose_name="Начало работы куратором", blank=True
    )
    curatoring_end_date = models.DateField(
        verbose_name="Конец работы куратором", blank=True
    )


    # @property
    # def start_date(self):
    #     if self.staff_position == 'Tracker':
    #         trackering_start_date = models.DateTimeField(
    #             verbose_name="Начало работы трекером", blank=True
    #         )
    #         trackering_end_date = models.DateTimeField(
    #             verbose_name="Конец работы трекером", blank=True
    #         )


    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.name} {self.last_name} -> {self.staff_position}"
