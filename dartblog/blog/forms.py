from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, UsernameField
from django.core.exceptions import ValidationError
from .utils import send_email_for_verify
from .models import User, Comment
from django import forms
from django.utils.translation import gettext_lazy as _
from mptt.forms import TreeNodeChoiceField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    widgets = {
        'username': forms.TextInput(attrs={"class": "form-control"}),
        'email': forms.EmailInput(attrs={"class": "form-control"}),
        'password1': forms.PasswordInput(attrs={"class": "form-control"}),
        'password2': forms.PasswordInput(attrs={"class": "form-control"})
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={"class": "form-control", "autofocus": True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email is not verify, check your email',
                    code="invalid_login",
                )

        return self.cleaned_data


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget = forms.HiddenInput()

    class Meta:
        model = Comment
        fields = ('content', 'parent')
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


    # 05    Каталог данных Роспатента
    # 12 	ИС Почты
    # 02 	ИС Компании по переработке вторсырья -
    # 16 	ИС Кафе быстрого питания
    # 11 	ИС для свопа
    # 13 	Сервис портфолио для программистов
    # 06 	Фитнес сервис