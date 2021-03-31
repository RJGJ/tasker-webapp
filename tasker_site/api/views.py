from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import *
from tasker_frontend.models import *


# Create your views here.
@api_view(['GET'])
def api_detail(request):
	data = {
		'API Overview' : 'api/',
		 
		# User
		'User endpoints reference': 'https://djoser.readthedocs.io/en/latest/base_endpoints.html',

		# # Company
		# 'Company List'      : 'api/company-list/',
		# 'Company Detail'    : 'api/company-detail/<int:pk>/',
		# 'Company Create'    : 'api/company-create/',
		# 'Company Update'    : 'api/company-update/<int:pk>/',
		# 'Company Delete'    : 'api/company-delete/<int:pk>/',

		# # Department
		# 'Department List'      : 'api/department-list/<int:pk>/',   # pk of company
		# 'Department Detail'    : 'api/department-detail/<int:pk>/',
		# 'Department Create'    : 'api/department-create/',
		# 'Department Update'    : 'api/department-update/<int:pk>/',
		# 'Department Delete'    : 'api/department-delete/<int:pk>/',

		# # Task
		# 'Task List'      : 'api/task-list/<int:pk1>/<int:pk2>/',    # pk of /company/department
		# 'Task Detail'    : 'api/task-detail/<int:pk>/',
		# 'Task Create'    : 'api/task-create/',
		# 'Task Update'    : 'api/task-update/<int:pk>/',
		# 'Task Delete'    : 'api/task-delete/<int:pk>/',

		# # Log
		# 'Log List'      : 'api/log-list/',
		# 'Log Detail'    : 'api/log-detail/<int:pk>/',
		# 'Log Create'    : 'api/log-create/',
	}

	return JsonResponse(data, safe=False)


# Project views ########################################################
# @api_view(['GET'])
# def project_list(request, pk):
# 	# task = Task.objects.filter(
#  #        Q(creator=user) | Q(taskers__in=[user,])
#  #    ).distinct()
# 	projects = Project.objects.filter(Q(owner=pk) | (Project.members.get(id__in=pk)))
# 	serializer = ProjectSerializer(projects, many=True)
# 	return Response(serializer.data)
 


# # Company views ######################################################
# @api_view(['GET'])
# def company_list(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def company_detail(request, pk):

#     # get token from header
#     # get user from token
#     # get tasks that belongs to the users department

#     company = Company.objects.get(id=pk)
#     serializer = CompanySerializer(company, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def company_create(request):
#     serializer = CompanySerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PATCH'])
# def company_update(request, pk):
#     try:
#         company = Company.objects.get(id=pk)
#         serializer = CompanySerializer(instance=company, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

#     except Company.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# @api_view(['DELETE'])
# def company_delete(request, pk):
#     try:
#         company = Company.objects.get(id=pk)
#         company.delete()
#         return Response(f'{company.name} is successfully deleted.')

#     except Company.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# # Department views ###################################################
# @api_view(['GET'])
# def department_list(request, pk=0):
#     ''' if pk=0 get all department 
#         if pk>0 get all department from a company '''

#     response = None
#     if int(pk) == 0:
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#         response = serializer.data
#     else:
#         try:
#             company = Company.objects.get(id=pk)
#             departments = Department.objects.get(company=company)
#             serializer = DepartmentSerializer(departments, many=True)
#             response = serializer.data

#         except Company.DoesNotExist:
#             response = f'Object with id:{pk} does not exist'

#     return Response(response)


# @api_view(['GET'])
# def department_detail(request, pk):
#     try:
#         department = Department.objects.get(id=pk)
#         serializer = DepartmentSerializer(department, many=False)
#         return Response(serializer.data)

#     except Department.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# @api_view(['POST'])
# def department_create(request):
#     serializer = DepartmentSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PATCH'])
# def department_update(request, pk):
#     try:
#         department = Department.objects.get(id=pk)
#         serializer = DepartmentSerializer(instance=department, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

#     except Department.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# @api_view(['DELETE'])
# def department_delete(request, pk):
#     try:
#         department = Department.objects.get(id=pk)
#         department.delete()
#         return Response(f'{department.name} is successfully deleted.')

#     except Department.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# # Task views #########################################################
# @api_view(['GET'])
# def task_list(request):

#     token = request.headers['Authorization'].split(' ')[1]
#     user = Token.objects.get(key=token).user
#     task = Task.objects.filter(
#         Q(creator=user) | Q(taskers__in=[user,])
#     ).distinct()

#     print(task)
#     serializer = TaskSerializer(task, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         serializer = TaskSerializer(task, many=False)
#         return Response(serializer.data)

#     except Task.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# @api_view(['POST'])
# def task_create(request):
#     serializer = TaskSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PATCH'])
# def task_update(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         serializer = TaskSerializer(instance=task, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

#     except Task.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# @api_view(['DELETE'])
# def task_delete(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return Response(f'{task.name} is successfully deleted.')

#     except Task.DoesNotExist:
#         return Response(f'Object with id:{pk} does not exist')


# Log views #########################################################
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
