from django.db import models


class Company(models.Model):

	def __str__(self):
		return self.name


class Department(models.Model):

	def __str__(self):
		return self.name


class Task(models.Model):

	def __str__(self):
		return self.name


class Log(models.Model):

	def __str__(self):
		return self.name
