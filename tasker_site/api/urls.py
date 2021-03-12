from django.urls import path, include

from .views import api_detail, company_detail

urlpatterns = [
	path('', api_detail),

	# accounts
	path('accounts/', include('djoser.urls')),
	path('accounts/', include('djoser.urls.authtoken')),

	# company
	path('company-detail/<str:pk>', company_detail, name='company-detail'),
]
