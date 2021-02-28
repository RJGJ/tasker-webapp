# Generated by Django 3.1.6 on 2021-02-27 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasker', '0019_auto_20210227_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]