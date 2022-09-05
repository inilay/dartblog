from django.urls import path, include
from django.views.generic import TemplateView

from .views import *
import django.contrib.auth.urls


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('password_reset/', UserPasswordReset.as_view(), name='reset_password'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('reset/<uidb64>/<token>/', EmailVerify.as_view(), name="verify_email"),
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html'), name='invalid_verify'),
    path('', include('django.contrib.auth.urls')),

]
