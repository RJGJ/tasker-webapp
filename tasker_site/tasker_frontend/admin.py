from django.contrib import admin

from .models import *


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'id']


class TeamAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'email']


class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'creation_date']


class TaskListAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'project']


class TaskListItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'parent_list', 'creation_date', 'due_date']


class LogAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'creator', 'project', 'creation_date']


models = {
	Project 		: ProjectAdmin,
	TaskList 		: TaskListAdmin,
	TaskListItem 	: TaskListItemAdmin,
	Log 			: LogAdmin,
	UserProfile		: UserProfileAdmin,
	Team			: TeamAdmin,
}

for model in models:
	admin.site.register(model, models[model])
