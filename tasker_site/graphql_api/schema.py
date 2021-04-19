import graphql
import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphene_django_cud.mutations.create import DjangoCreateMutation
from graphene_django_cud.mutations.delete import DjangoDeleteMutation
from graphene_django_cud.mutations.patch import DjangoPatchMutation
from graphene_django_cud.util import disambiguate_id
from graphql_auth import mutations
from graphql_auth.schema import MeQuery, UserQuery
from graphql_jwt import Refresh, Verify
from graphql_jwt.decorators import login_required
from tasker_frontend.models import *

########## START TYPES ############################################################


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


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
class ProjectCreateMutation(DjangoCreateMutation):
    class Meta:
        model = Project
        login_required = True


class TeamCreateMutation(DjangoCreateMutation):
    class Meta:
        model = Team
        login_required = True


# Patch Mutations
class ProjectPatchMutation(DjangoPatchMutation):
    class Meta:
        model = Project
        login_required = True


class TeamPatchMutation(DjangoPatchMutation):
    class Meta:
        model = Team
        login_required = True
    
    @classmethod
    def mutate(cls, root, info, input, id):

        print(input)

        team = Team.objects.filter(id=id)[0]
        user = User.objects.get(id=info.context.user.id)

        if user in getattr(team, 'adminIDs').all():
            return super().mutate(root, info, input, id)

        return graphql.error.GraphQLError("You do not have permission to access this mutation")


# Delete Mutations
class ProjectDeleteMutation(DjangoDeleteMutation):
    class Meta:
        model = Project
        login_required = True


class TeamDeleteMutation(DjangoDeleteMutation):
    class Meta:
        model = Team
        login_required = True
    
    @classmethod
    def mutate(cls, root, info, id):

        team = Team.objects.filter(id=id)[0]
        user = User.objects.get(id=info.context.user.id)

        if user in getattr(team, 'adminIDs').all():
            return super().mutate(root, info, id)

        return graphql.error.GraphQLError("You do not have permission to access this mutation")


# Other
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


########## END MUTATIONS ############################################################


class Query(UserQuery, MeQuery, graphene.ObjectType):

    viewer = graphene.Field(UserType, token=graphene.String(required=True))
    projects_by_user = graphene.List(
        ProjectType,
        pk=graphene.Int(required=True),
        token=graphene.String(required=True),
    )

    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user

    @login_required
    def resolve_projects_by_user(root, info, pk, **kwargs):
        # get all projects that the user is a member
        return Project.objects.filter(members__id=pk)


class MyMutation(AuthMutation, graphene.ObjectType):
    
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()

    # team
    create_team = TeamCreateMutation.Field()
    patch_team = TeamPatchMutation.Field()
    delete_team = TeamDeleteMutation.Field()

    # project
    create_project = ProjectCreateMutation.Field()
    patch_project = ProjectPatchMutation.Field()
    delete_project = ProjectDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutation)
