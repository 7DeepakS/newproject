from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('protected_view')
    return render(request, 'myapp/login.html')

@login_required
def protected_view(request):
    return render(request, 'myapp/protected.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

