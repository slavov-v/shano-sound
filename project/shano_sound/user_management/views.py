from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from hashlib import sha256
from django.views.generic import View, CreateView, ListView, TemplateView, FormView
from django.utils.decorators import method_decorator
from user_management.models import User
from user_management.forms import RegisterAndLoginForm, AddFriendForm
from user_management.helpers import session_exists
from user_management.decorators import login_required
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
            # import ipdb; ipdb.set_trace()
            return redirect('/register')
        else:
            if User.validate_password(request.POST['email'], request.POST['password']):
                request.session['email'] = request.POST['email']
                return redirect('/profile')
            else:
                error = "Invalid password"
    if request.method == 'GET':
        # import ipdb; ipdb.set_trace()
        login_form = RegisterAndLoginForm()
        if session_exists(request):
            return redirect('/profile')
        return render(request, 'login_form.html', locals())

# def temp_profile_view(request, *args, **kwargs):
#     user_email = request.session['email']
#     return render(request, 'profile_page.html', locals())


def log_out_view(request):
    request.session.flush()
    return redirect('/login')

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = 'profile_page.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['session_email'] = self.request.session['email']
        return context


@method_decorator(login_required, name="dispatch")
class AddFriendView(View):

    def get(self, request):
        form = AddFriendForm()
        return render(request, 'add_friend.html', locals())

    def post(self, request):
        form = AddFriendForm(request.POST)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            try:
                form.save(email=request.session['email'])
            except:
                errors = "User does not exist"
                return render(request, 'add_friend.html', locals())
        return redirect('/profile')

@method_decorator(login_required, name="dispatch")
class FriendListView(ListView):
    template_name = 'friends.html'

    def get_queryset(self):
        qs = User.objects.get(email=self.request.session.get('email')).friends.all()
        # import ipdb; ipdb.set_trace()
        return qs
