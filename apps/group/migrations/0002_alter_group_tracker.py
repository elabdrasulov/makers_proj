# Generated by Django 4.1.1 on 2022-10-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='tracker',
            field=models.ManyToManyField(related_name='trackers', to='staff.staff'),
        ),
    ]
