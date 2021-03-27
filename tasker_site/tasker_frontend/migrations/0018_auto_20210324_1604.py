# Generated by Django 3.1.6 on 2021-03-24 08:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasker_frontend', '0017_auto_20210317_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_type',
        ),
        migrations.AlterField(
            model_name='log',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 16, 4, 51, 497299)),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 16, 4, 51, 492308)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasker_frontend.company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasker_frontend.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]