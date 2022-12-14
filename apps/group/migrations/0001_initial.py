# Generated by Django 4.1.1 on 2022-10-11 17:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_group', models.CharField(max_length=50)),
                ('date_of_start', models.DateField(blank=True, choices=[], null=True)),
                ('date_of_end', models.DateField(blank=True, null=True)),
                ('group_studying_time', models.CharField(blank=True, choices=[('day', 'day'), ('evening', 'evening')], max_length=20, null=True)),
                ('number_of_students', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(36)])),
                ('mentor', models.ForeignKey(default='Ментор пока не определен', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='groups_mentor', to='staff.staff')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_room', to='room.room')),
                ('tracker', models.ManyToManyField(related_name='trackers', to='staff.staff')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
