# Generated by Django 4.1.1 on 2022-10-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_group', models.CharField(max_length=50)),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('group_studying_time', models.CharField(max_length=20)),
                ('mentor', models.ManyToManyField(related_name='groups', to='staff.staff')),
                ('tracker', models.ManyToManyField(related_name='trackers', to='staff.staff')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
