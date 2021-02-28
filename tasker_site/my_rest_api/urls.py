from django.urls import path
from .views import (
    api_overview,
    task_list,
    task_detail,
    task_create,
    task_update,
    task_delete,
    task_subtasks,
    user_list,
    user_detail,
    user_update,
)

urlpatterns = [
    path('', api_overview, name='api-overview'),

    # Task
    path('task-list/', task_list, name='task-list'),
    path('task-detail/<str:pk>/', task_detail, name='task-detail'),
    path('task-create/', task_create, name='task-create'),
    path('task-update/<str:pk>/', task_update, name='task-update'),
    path('task-delete/<str:pk>/', task_delete, name='task-delete'),
    path('task-subtasks/<str:pk>/', task_subtasks, name='task-subtasks'),

    # User
    path('user-list/', user_list, name='user-list'),
    path('user-detail/<str:pk>/', user_detail, name='user-detail'),
    path('user-update/<str:pk>/', user_update, name='user-update'),
]