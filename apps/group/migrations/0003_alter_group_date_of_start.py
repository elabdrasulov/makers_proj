# Generated by Django 4.1.1 on 2022-10-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_is_graduated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_of_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
