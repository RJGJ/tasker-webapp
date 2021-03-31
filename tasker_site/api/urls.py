from django.urls import path, include

from .views import *


urlpatterns = [
	path('', api_detail),

	# accounts
	path('accounts/', include('djoser.urls')),
	path('accounts/', include('djoser.urls.authtoken')),

	# project
	# path('project-list/<int:pk>/', project_list, name='project_list'),


	# # company
	# path('company-list/', company_list, name='company-list'),
	# path('company-detail/<int:pk>/', company_detail, name='company-detail'),
	# path('company-create/', company_create, name='company-create'),
	# path('company-update/<int:pk>/', company_update, name='company-update'),
	# path('company-delete/<int:pk>/', company_delete, name='company-delete'),

	# # department
	# path('department-list/<int:pk>/', department_list, name='department-list'),
	# path('department-detail/<int:pk>/', department_detail, name='department-detail'),
	# path('department-create/', department_create, name='department-create'),
	# path('department-update/<int:pk>/', department_update, name='department-update'),
	# path('department-delete/<int:pk>/', department_delete, name='department-delete'),

	# # task
	# path('task-list/', task_list, name='task-list'),
	# path('task-detail/<int:pk>/', task_detail, name='task-detail'),
	# path('task-create/', task_create, name='task-create'),
	# path('task-update/<int:pk>/', task_update, name='task-update'),
	# path('task-delete/<int:pk>/', task_delete, name='task-delete'),

	# # log
	# path('log-list/', log_list, name='log-list'),
	# path('log-detail/<int:pk>/', log_detail, name='log-detail'),
	# path('log-create/', log_create, name='log-create'),
]
