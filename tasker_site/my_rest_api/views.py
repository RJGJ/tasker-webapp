from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer, UserSerializer
from tasker.models import Task


# Create your views here.
@api_view(['GET'])
def api_overview(request):

    api_urls = {

        # Task
        'Task List': '/task-list/',
        'Task Detail View': '/task-detail/<str:pk>',
        'Task Create': '/task-create/',
        'Task Update': '/task-update/<str:pk>',
        'Task Delete': '/task-delete/<str:pk>',
        'Task List Subtasks': '/task-subtasks/<str:pk>',

        # User
        'User List': '/user-list/',
        'User Detail View': '/user-detail/<str:pk>',
        'User Update': '/user-update/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):

    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item successfully deteted')


@api_view(['GET'])
def task_subtasks(request, pk):

    tasks = Task.objects.filter(parent=pk)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# User
@api_view(['GET'])
def user_list(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):

    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def user_update(request, pk):

    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
