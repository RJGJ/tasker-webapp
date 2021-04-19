from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from datetime import datetime as dt


class UserProfile(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class Team(models.Model):

	name 		= models.CharField(max_length=254, null=False, default="Team name")
	description = models.CharField(max_length=254, null=False, default="Team description")
	email 		= models.EmailField(max_length=254)
	members 	= models.ManyToManyField(User, related_name="members")
	adminIDs 	= models.ManyToManyField(User, related_name="adminIDs")

	def __str__(self):
		return self.name


class Project(models.Model):

	title 			= models.CharField(max_length=254, null=False, default=None)
	description 	= models.CharField(max_length=500, null=True)
	team 			= models.ForeignKey(Team, on_delete=models.CASCADE, default=None, null=False)
	members 		= models.ManyToManyField(User, related_name='owner', blank=True)
	creation_date 	= models.DateTimeField(default=dt.now())

	def __str__(self):
		return self.title


class TaskList(models.Model):

	title 			= models.CharField(max_length=254, null=False, default=None)
	description 	= models.CharField(max_length=500, null=True)
	project 		= models.ForeignKey(Project, on_delete=models.CASCADE, default=None )

	def __str__(self):
		return self.title


class TaskListItem(models.Model):

	title 			= models.CharField(max_length=254, null=False, default=None)
	description 	= models.CharField(max_length=500, null=True)
	parent_list 	= models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None)
	assingned_to 	= models.ManyToManyField(User, blank=True)
	creation_date 	= models.DateTimeField(default=dt.now())
	due_date 		= models.DateTimeField(default=None, null=True, blank=True)
	finished 		= models.BooleanField(default=False)

	def __str__(self):
		return self.title


class Log(models.Model):

	title 			= models.CharField(max_length=254, null=False, default=None)
	description 	= models.CharField(max_length=500, null=True)
	creator 		= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	project			= models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
	creation_date	= models.DateTimeField(default=dt.now())

	def __str__(self):
		return self.title
