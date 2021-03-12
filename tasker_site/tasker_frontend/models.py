from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from datetime import datetime as dt


'''
company and departments will have an company/department admin(s)
task can be created with:
    company to company
    company to department
    department to department
    department to user
    user to department (with approval from department admin)
    user to user (with approval from departmen admin and acceptance from recieving user)
'''


class Company(models.Model):

    _phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    name 		= models.CharField(max_length=200, null=False, default=None)
    description = models.CharField(max_length=500, null=True)
    email 		= models.EmailField(max_length=200, null=False, default=None)
    phone 		= models.CharField(validators=[_phone_regex,], max_length=200, null=False, default=None)
    address 	= models.CharField(max_length=500, null=False, default=None)

    def __str__(self):
        return self.name


class Department(models.Model):

    name 		= models.CharField(max_length=200, null=False, default=None)
    description = models.CharField(max_length=500, null=True)
    company		= models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Task(models.Model):
    
    COMPANY_TO_COMPANY = 1
    COMPANY_TO_DEPARTMENT = 2
    DEPARTMENT_TO_DEPARTMENT = 3
    DEPARTMENT_TO_USER = 4
    USER_TO_DEPARTMENT = 5
    USER_TO_USER = 6

    name 			= models.CharField(max_length=200, null=False, default=None)
    description 	= models.CharField(max_length=500, null=True)
    task_type 		= models.IntegerField(default=USER_TO_USER)
    creator 		= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    creation_date	= models.DateTimeField(default=dt.now())
    due_date		= models.DateTimeField(default=None)

    def __init__(self):
        taskers		= models.ManyToManyField(User, related_name=self.creator)

    def __str__(self):
        return self.name


class Log(models.Model):

    title = models.CharField(max_length=500, null=False, default=None)
    description 	= models.CharField(max_length=500, null=True)
    creator 		= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task			= models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    creation_date	= models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.name
