from django.urls import path
from django.views.generic.base import TemplateView

from .views import index

urlpatterns = [
	# path('register/', register, name='register'),
	path('', index, name="index"),
]