from django.urls import path, include

from .views import api_detail

urlpatterns = [
	path('', api_detail),
	path('accounts/', include('djoser.urls')),
	path('accounts/', include('djoser.urls.authtoken')),
]
