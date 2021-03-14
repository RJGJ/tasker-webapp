from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import CompanySerializer, DepartmentSerializer, TaskSerializer, LogSerializer
from tasker_frontend.models import Company, Department, Task, Log


# Create your views here.
@api_view(['GET'])
def api_detail(request):
    data = {
        'API Overview' : 'api/',
        
        # User
        'User endpoints reference': 'https://djoser.readthedocs.io/en/latest/base_endpoints.html',

        # Company
        'Company List'      : 'api/company-list/',
        'Company Detail'    : 'api/company-detail/<str:pk>/',
        'Company Create'    : 'api/company-create/',
        'Company Update'    : 'api/company-update/<str:pk>/',
        'Company Delete'    : 'api/company-delete/<str:pk>/',

        # Department
        'Department List'      : 'api/department-list/<str:pk>/',   # pk of company
        'Department Detail'    : 'api/department-detail/<str:pk>/',
        'Department Create'    : 'api/department-create/',
        'Department Update'    : 'api/department-update/<str:pk>/',
        'Department Delete'    : 'api/department-delete/<str:pk>/',

        # Task
        'Task List'      : 'api/task-list/<str:pk1>/<str:pk2>/',    # pk of /company/department
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


# Company views ######################################################
@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def company_detail(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def company_create(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PATCH'])
def company_update(request, pk):
    try:
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(instance=company, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except Company.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['DELETE'])
def company_delete(request, pk):
    try:
        company = Company.objects.get(id=pk)
        company.delete()
        return Response(f'{company.name} is successfully deleted.')

    except Company.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


# Department views ###################################################
@api_view(['GET'])
def department_list(request, pk=0):
    ''' if pk=0 get all department 
        if pk>0 get all department from a company '''

    response = None
    if int(pk) == 0:
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        response = serializer.data
    else:
        try:
            company = Company.objects.get(id=pk)
            departments = Department.objects.get(company=company)
            serializer = DepartmentSerializer(departments, many=True)
            response = serializer.data

        except Company.DoesNotExist:
            response = f'Object with id:{pk} does not exist'

    return Response(response)


@api_view(['GET'])
def department_detail(request, pk):
    try:
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(department, many=False)
        return Response(serializer.data)

    except Department.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['POST'])
def department_create(request):
    serializer = DepartmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PATCH'])
def department_update(request, pk):
    try:
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=department, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except Department.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['DELETE'])
def department_delete(request, pk):
    try:
        department = Department.objects.get(id=pk)
        department.delete()
        return Response(f'{department.name} is successfully deleted.')

    except Department.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


# Task views #########################################################
@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    except Task.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PATCH'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except Task.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(f'{task.name} is successfully deleted.')

    except Task.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


# Task views #########################################################
@api_view(['GET'])
def log_list(request):
    log = Log.objects.all()
    serializer = LogSerializer(log, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def log_detail(request, pk):
    try:
        log = Log.objects.get(id=pk)
        serializer = LogSerializer(log, many=False)
        return Response(serializer.data)

    except Log.DoesNotExist:
        return Response(f'Object with id:{pk} does not exist')


@api_view(['POST'])
def log_create(request):
    serializer = LogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
