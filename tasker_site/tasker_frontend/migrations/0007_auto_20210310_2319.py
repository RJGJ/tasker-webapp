# Generated by Django 3.1.6 on 2021-03-10 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker_frontend', '0006_auto_20210310_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 23, 19, 48, 998473)),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 23, 19, 48, 982846)),
        ),
    ]