from django.contrib.auth.models import User

from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

from graphene_django_cud.mutations.create import DjangoCreateMutation
from graphene_django_cud.mutations.patch import DjangoPatchMutation
from graphene_django_cud.mutations.delete import DjangoDeleteMutation

from tasker_frontend.models import *

import graphene

########## START TYPES ############################################################


class UserInputType(graphene.InputObjectType):
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


# Create Mutations
class ProjectUpdateMutation(DjangoCreateMutation):
    class Meta:
        model = Project


# Patch Mutations
class ProjectPatchMutation(DjangoPatchMutation):
    class Meta:
        model = Project


# Delete Mutations
class ProjectDeleteMutation(DjangoDeleteMutation):
    class Meta:
        model = Project


# Other
class AuthMutation(graphene.ObjectType):
    register                    = mutations.Register.Field()
    verify_account              = mutations.VerifyAccount.Field()
    token_auth                  = mutations.ObtainJSONWebToken.Field()
    update_account              = mutations.UpdateAccount.Field()
    resend_activation_email     = mutations.ResendActivationEmail.Field()
    send_password_reset_email   =   mutations.SendPasswordResetEmail.Field()
    password_reset              = mutations.PasswordReset.Field()


########## END MUTATIONS ############################################################


class Query(UserQuery, MeQuery, graphene.ObjectType):

    projects_by_user = graphene.List(ProjectType, pk=graphene.Int(required=True))

    def resolve_projects_by_user(root, info, pk):
        return Project.objects.filter(owner__id=pk)


class MyMutation(AuthMutation, graphene.ObjectType):

    create_project = ProjectUpdateMutation.Field()
    patch_project = ProjectPatchMutation.Field()
    delete_project = ProjectDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutation)
