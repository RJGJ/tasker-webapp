from django.contrib.auth.models import User

from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

from tasker_frontend.models import *

import graphene

########## START TYPES ############################################################


class UserType(graphene.InputObjectType):
    id = graphene.ID()


class ProjectType(DjangoObjectType):
	class Meta:
		model = Project


class TaskListType(DjangoObjectType):
	class Meta:
		model = TaskList


class TaskListItemType(DjangoObjectType):
	class Meta:
		model = TaskListItem


class LogType(DjangoObjectType):
	class Meta:
		model = Log


########## END TYPES ################################################################

########## START MUTATIONS ##########################################################


class ProjectMutation(graphene.Mutation):

	class Arguments:
		id 				= graphene.ID(required=True)
		new_title 		= graphene.String()
		owner 			= graphene.ID()
		members 		= graphene.List(UserType)
		creation_date 	= graphene.String()	# change to proper python datetime before save


	project = graphene.Field(ProjectType)

	@classmethod
	def mutate(self, root, info , new_title):
		project = Project(title=new_title)
		project.save()


class AuthMutation(graphene.ObjectType):
	register 					= mutations.Register.Field()
	verify_account 				= mutations.VerifyAccount.Field()
	token_auth 					= mutations.ObtainJSONWebToken.Field()
	update_account 				= mutations.UpdateAccount.Field()
	resend_activation_email 	= mutations.ResendActivationEmail.Field()
	send_password_reset_email 	=	mutations.SendPasswordResetEmail.Field()
	password_reset 				= mutations.PasswordReset.Field()


########## END MUTATIONS ############################################################


class Query(UserQuery, MeQuery, graphene.ObjectType):

	projects_by_user = graphene.List(ProjectType, pk=graphene.Int(required=True))

	def resolve_projects_by_user(root, info, pk):
		return Project.objects.filter(owner__id=pk)


class MyMutation(AuthMutation, graphene.ObjectType):

	# update_project = ProjectMutation.Field()
	pass


schema = graphene.Schema(query=Query, mutation=MyMutation)
