from graphene_django import DjangoObjectType

from tasker_frontend.models import *
from django.contrib.auth.models import User
from tasker_frontend.models import *

import graphene


class ProjectType(DjangoObjectType):
	class Meta:
		model = Project


class UserType(DjangoObjectType):
	class Meta:
		model = User


class TaskListType(DjangoObjectType):
	class Meta:
		model = TaskList


class TaskListItemType(DjangoObjectType):
	class Meta:
		model = TaskListItem


class LogType(DjangoObjectType):
	class Meta:
		model = Log


class Query(graphene.ObjectType):

	projects_by_user = graphene.List(ProjectType, pk=graphene.Int(required=True))
	all_users = graphene.Field(UserType, id=graphene.Int(required=True))

	def resolve_projects_by_user(root, info, pk):
		return Project.objects.filter(owner__id=pk)

	def resolve_all_users(root, info, id):
		return User.objects.get(id=id)


class ProjectMutation(graphene.Mutation):

	class Arguments:
		new_title = graphene.String(required=True)

	project = graphene.Field(ProjectType)

	@classmethod
	def mutate(self, root, info , new_title):
		project = Project(title=new_title)
		project.save()


class MyMutation(graphene.ObjectType):

	update_projects = ProjectMutation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutation)
