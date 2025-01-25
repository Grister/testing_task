from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'image', 'password1', 'password2')

    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Enter your username"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'placeholder': "Enter your email"
        })
    )
    image = forms.FileField(
        required=False,
        label="Profile Photo",
        widget = forms.ClearableFileInput(attrs={
            'class': "form-control",
            'accept': "image/*",
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Enter your password"
        })
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Confirm your password"
        })
    )

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        try:
            UserModel.objects.get(email=email)
            raise ValidationError("Email is already registered")
        except UserModel.DoesNotExist:
            return email


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': "Enter your username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Enter your password"
        })
    )
