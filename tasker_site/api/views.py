from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import CompanySerializer
from tasker_frontend.models import Company, Department, Task, Log


# Create your views here.
@api_view(['GET'])
def api_detail(request):
    data = {
        'API Overview' : 'api/',
        
        # User
        'refer to this': 'https://djoser.readthedocs.io/en/latest/base_endpoints.html',

        # Company
        'Company List'      : 'api/company-list/',
        'Company Detail'    : 'api/company-detail/<str:pk>/',
        'Company Create'    : 'api/company-create/',
        'Company Update'    : 'api/company-update/<str:pk>/',
        'Company Delete'    : 'api/company-delete/<str:pk>/',

        # Department
        'Department List'      : 'api/department-list/',
        'Department Detail'    : 'api/department-detail/<str:pk>/',
        'Department Create'    : 'api/department-create/',
        'Department Update'    : 'api/department-update/<str:pk>/',
        'Department Delete'    : 'api/department-delete/<str:pk>/',

        # Task
        'Task List'      : 'api/task-list/',
        'Task Detail'    : 'api/task-detail/<str:pk>/',
        'Task Create'    : 'api/task-create/',
        'Task Update'    : 'api/task-update/<str:pk>/',
        'Task Delete'    : 'api/task-delete/<str:pk>/',

        # Log
        'Log List'      : 'api/log-list/',
        'Log Detail'    : 'api/log-detail/<str:pk>/',
        'Log Create'    : 'api/log-create/',
    }
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def company_detail(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)

    return Response(serializer.data)
