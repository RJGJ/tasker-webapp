from django.contrib import admin

from .models import Company, Department, Task, Log


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'company']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'creation_date', 'due_date']


class LogAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'task', 'creation_date']


models = {
    Company     : CompanyAdmin,
    Department  : DepartmentAdmin,
    Task        : TaskAdmin,
    Log         : LogAdmin,
}

for model in models:
    admin.site.register(model, models[model])
