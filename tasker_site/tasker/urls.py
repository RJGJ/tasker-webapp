from django.urls import path

from . import views

urlpatterns = [
    # /tasker/register/
    path('register/', views.register, name='register'),
    # /tasker/login/
    path('login/', views.login_user, name='login'),
    # /tasker/logout/
    path('logout/', views.logout_user, name='logout'),
    # /tasker/dashboard/
    path('dashboard/', views.dashboard, name='dashboard'),
]
