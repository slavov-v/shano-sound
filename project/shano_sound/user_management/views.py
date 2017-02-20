from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from hashlib import sha256
from django.views.generic import View, CreateView, ListView
from user_management.models import User
from user_management.forms import RegisterAndLoginForm
from user_management.helpers import session_exists
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        reg_form = RegisterAndLoginForm(request.POST)
        if not User.exists(request.POST['email']):
            if reg_form.is_valid():
                reg_form.hash_password()
                reg_form.save()
            return redirect('/login')
        else:
            return render(request, 'register_form.html', locals())
            error = "User already exists"
    else:
        reg_form = RegisterAndLoginForm()
        return render(request, 'register_form.html', locals())


def login_view(request):
    if request.method == 'POST':
        login_form = RegisterAndLoginForm(request.POST)
        if not User.exists(request.POST['email']):
            import ipdb; ipdb.set_trace()
            return redirect('/register')
        else:
            if User.validate_password(request.POST['email'], request.POST['password']):
                request.session['email'] = request.POST['email']
                return temp_profile_view(request)
            else:
                error = "Invalid password"
    if request.method == 'GET':
        # import ipdb; ipdb.set_trace()
        login_form = RegisterAndLoginForm()
        if session_exists(request):
            return temp_profile_view(request)
        return render(request, 'login_form.html', locals())

def temp_profile_view(request, *args, **kwargs):
    user_email = request.session['email']
    return render(request, 'profile_page.html', locals())
