from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """
    Task Model

    fields:
        name: CharField
        creator: ForeignKey(Users)
        creation_date: DateTimeField
        active: BooleanField(default=True)
        target_date: DateTimeField
        description: CharField
        subtasks: ForeignKey(self)
        taskers: ForeignKey(Users)
    """

    name = models.CharField(max_length=200, null=False)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='self',
        default=None
    )

    creation_date = models.DateTimeField(
        'date created',
        default=timezone.now
    )

    active = models.BooleanField(default=True)

    target_date = models.DateTimeField(
        'target_date',
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    # parent task
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    taskers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


def task_exempt_creator(sender,  instance, action, reverse, *args, **kwargs):
    '''
    Removes the task creator from taskers field
    '''
    if  action is 'post_add':
        creator = User.objects.filter(pk=instance.creator.pk)
        instance.taskers.remove(creator[0])


m2m_changed.connect(task_exempt_creator, sender=Task.taskers.through)
