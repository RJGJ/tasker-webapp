# Generated by Django 3.1.6 on 2021-02-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0015_auto_20210224_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='level',
        ),
        migrations.RemoveField(
            model_name='task',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='task',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tree_id',
        ),
    ]