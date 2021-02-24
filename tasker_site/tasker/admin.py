from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    exclude = [
        'level',
        'lft',
        'rght',
        'tree_id'
    ]
    list_display = (
        'name',
        'creator',
        'creation_date',
        'target_date',
        'active',
        'parent'
    )

# Register your models here.
admin.site.register(Task, TaskAdmin)
