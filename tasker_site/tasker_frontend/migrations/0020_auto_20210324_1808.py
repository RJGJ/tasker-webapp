# Generated by Django 3.1.6 on 2021-03-24 10:08

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasker_frontend', '0019_auto_20210324_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 18, 8, 36, 726449)),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 18, 8, 36, 722460)),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskers',
            field=models.ManyToManyField(default=None, related_name='creators', to=settings.AUTH_USER_MODEL),
        ),
    ]
