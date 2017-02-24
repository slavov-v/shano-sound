from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from hashlib import sha256
from django.views.generic import View, CreateView, ListView, TemplateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from user_management.models import BaseUser
from user_management.forms import RegisterAndLoginForm, AddFriendForm, LoginForm
from user_management.helpers import session_exists
# from user_management.decorators import login_required
# Create your views here.


class RegisterView(FormView):
    template_name = 'register_form.html'
    form_class = RegisterAndLoginForm

    def form_valid(self, form):
        # import ipdb; ipdb.set_trace()
        user = form.save()
        return redirect('/login')


# def register_view(request):
#     if request.method == 'POST':
#         reg_form = RegisterAndLoginForm(request.POST)
#         if not User.exists(request.POST['email']):
#             if reg_form.is_valid():
#                 reg_form.hash_password()
#                 reg_form.save()
#             return redirect('/login')
#         else:
#             return render(request, 'register_form.html', locals())
#             error = "User already exists"
#     else:
#         reg_form = RegisterAndLoginForm()
#         return render(request, 'register_form.html', locals())

class LoginView(FormView):
    template_name = 'login_form.html'
    form_class = LoginForm
    # success_url = '/profile'

    def get_success_url(self):
        url = self.request.GET.get('next', '/profile')
        return url

    def dispatch(self, *args, **kwargs):
        self.error = None
        # import ipdb; ipdb.set_trace()
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password, username=email)
        import ipdb; ipdb.set_trace()

        if user is None:
            self.error = "Invalid email or password"
            return self.form_invalid(form)

        # if not user.is_active:
        #     self.error = "Activate"
        #     return self.form_invalid(form)

        login(self.request, user)
        # import ipdb; ipdb.set_trace()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = self.error
        return context

# def login_view(request):
#     if request.method == 'POST':
#         login_form = RegisterAndLoginForm(request.POST)
#         if not User.exists(request.POST['email']):
#             # import ipdb; ipdb.set_trace()
#             return redirect('/register')
#         else:
#             if User.validate_password(request.POST['email'], request.POST['password']):
#                 request.session['email'] = request.POST['email']
#                 return redirect('/profile')
#             else:
#                 error = "Invalid password"
#     if request.method == 'GET':
#         # import ipdb; ipdb.set_trace()
#         login_form = RegisterAndLoginForm()
#         if session_exists(request):
#             return redirect('/profile')
#         return render(request, 'login_form.html', locals())

# def temp_profile_view(request, *args, **kwargs):
#     user_email = request.session['email']
#     return render(request, 'profile_page.html', locals())

@login_required
def log_out_view(request):
    logout(request)
    return redirect('/login')

# @method_decorator(login_required, name="dispatch")
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_page.html'

# @method_decorator(login_required, name="dispatch")
class AddFriendView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddFriendForm()
        return render(request, 'add_friend.html', locals())

    def post(self, request):
        form = AddFriendForm(request.POST)
        import ipdb; ipdb.set_trace()
        if form.is_valid():
            try:
                form.save(email=request.user.email)
            except:
                errors = "User does not exist"
                return render(request, 'add_friend.html', locals())
        return redirect('/profile')

# @method_decorator(login_required, name="dispatch")
class FriendListView(LoginRequiredMixin, ListView):
    template_name = 'friends.html'

    def get_queryset(self):
        qs = BaseUser.objects.get(email=self.request.user.email).friends.all()
        # import ipdb; ipdb.set_trace()
        return qs
