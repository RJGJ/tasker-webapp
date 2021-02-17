from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users


# Create your views here.

@unauthenticated_user
def register(request):
   
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was registered for {user}!')

            return redirect('login')

    context = {'form': form}
    return render(request, 'tasker/register.html', context)


@unauthenticated_user
def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Username of Password is incorrect.')

    context = {}
    return render(request, 'tasker/login.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def dashboard(request):
    context = {}
    return render(request, 'tasker/dashboard.html', context)
