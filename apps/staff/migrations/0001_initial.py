# Generated by Django 4.1.1 on 2022-10-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff/', verbose_name='Фотография')),
                ('direction', models.CharField(blank=True, choices=[('Py', 'Python'), ('JS', 'Javascript')], max_length=50, null=True, verbose_name='Направление')),
                ('staff_position', models.CharField(choices=[('Curator', 'Куратор'), ('Mentor', 'Ментор'), ('Tracker', 'Трекер')], max_length=20, verbose_name='Должность')),
                ('start_of_training', models.DateField(blank=True, null=True, verbose_name='Начало стажировки')),
                ('end_of_training', models.DateField(blank=True, null=True, verbose_name='Конец стажировки')),
                ('notes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Дополнительно(заметки)')),
                ('trackering_start_date', models.DateField(blank=True, verbose_name='Начало работы трекером')),
                ('trackering_end_date', models.DateField(blank=True, verbose_name='Конец работы трекером')),
                ('mentoring_start_date', models.DateField(blank=True, verbose_name='Начало работы ментором')),
                ('mentoring_end_date', models.DateField(blank=True, verbose_name='Конец работы ментором')),
                ('curatoring_start_date', models.DateField(blank=True, verbose_name='Начало работы куратором')),
                ('curatoring_end_date', models.DateField(blank=True, verbose_name='Конец работы куратором')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
