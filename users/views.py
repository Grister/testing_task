from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import UserRegistrationForm, UserLoginForm


class UserRegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm

    def get_success_url(self):
        return reverse('users:sign_in')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('/blog/')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = '/blog/'
    next_page = '/blog/'
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    next_page = '/sign-in/'
