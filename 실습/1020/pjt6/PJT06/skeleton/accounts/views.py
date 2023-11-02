from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import CustomCreationForm


# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@require_http_methods(["POST"])
def logout(request):
    if request.method=='POST':
        auth_logout(request)
    return redirect('boards:index')


@login_required
@require_http_methods(["POST"])
def follow(request, user_pk):
    pass