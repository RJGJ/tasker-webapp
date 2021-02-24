# Generated by Django 3.1.6 on 2021-02-24 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0014_auto_20210224_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='parent',
        ),
        migrations.AddField(
            model_name='task',
            name='parent_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasker.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]