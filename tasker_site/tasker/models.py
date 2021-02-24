from django.db import models
from django.conf import settings
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey



# Create your models here.
class Task(MPTTModel):
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
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='childred'
    )

    level = models.PositiveIntegerField(default=0)
    lft = models.PositiveIntegerField(default=0)
    rght = models.PositiveIntegerField(default=0)
    tree_id = models.PositiveIntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['name']

    # subtasks = models.ManyToManyField('self', blank=True)

    # taskers = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     blank=True,
    #     default=None
    # )

    def __str__(self):
        return self.name
