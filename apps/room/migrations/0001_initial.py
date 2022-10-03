# Generated by Django 4.1.1 on 2022-10-03 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('room_status', models.BooleanField(default=False)),
                ('mentor', models.ForeignKey(default='кабинет свободен', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='rooms', to='staff.staff')),
            ],
        ),
    ]
