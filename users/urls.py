from django.urls import path
from .views import UserRegistrationView, UserLogoutView, UserLoginView

app_name = 'users'

urlpatterns = [
    path('sign-up/', UserRegistrationView.as_view(), name='sign_up'),
    path('sign-in/', UserLoginView.as_view(), name='sign_in'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
