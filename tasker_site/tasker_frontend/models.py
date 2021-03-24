from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from datetime import datetime as dt


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

    name 			= models.CharField(max_length=200, null=False, default=None)
    description 	= models.CharField(max_length=500, blank=True, default=None)
    creator 		= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    creation_date	= models.DateTimeField(default=dt.now())
    due_date		= models.DateTimeField(default=None, null=True, blank=True)
    taskers         = models.ManyToManyField(User, related_name='creators', blank=True)

    def __str__(self):
        return self.name


class Log(models.Model):

    title           = models.CharField(max_length=500, null=False, default=None)
    description 	= models.CharField(max_length=500, null=True)
    creator 		= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task			= models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    creation_date	= models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
