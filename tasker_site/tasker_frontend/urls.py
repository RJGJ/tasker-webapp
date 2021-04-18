from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
	path('', TemplateView.as_view(template_name="index.html")),
	path('login/', TemplateView.as_view(template_name="login.html")),
	path('register/', TemplateView.as_view(template_name="register.html")),
	path('dashboard/', TemplateView.as_view(template_name="dashboard.html")),
	path('account-settings/', TemplateView.as_view(template_name="account-settings.html")),
]