from django.urls import path
from .views import api_overview, task_list

urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('task-list/', task_list, name='task-list'),
]