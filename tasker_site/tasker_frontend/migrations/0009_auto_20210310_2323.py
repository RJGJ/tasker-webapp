# Generated by Django 3.1.6 on 2021-03-10 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasker_frontend', '0008_auto_20210310_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 15, 23, 53, 197253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 15, 23, 53, 197253, tzinfo=utc)),
        ),
    ]
