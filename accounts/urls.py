"""
Script to Define the urls related to accounts
"""
# pylint: disable=import-error
# pylint: disable=invalid-name

from django.urls import path
from .views import (
    SignUpView,
    LoginView,
    LogOutView,
)


urlpatterns = [
    path(
        'register/',
        SignUpView.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login_view'
    ),
    path(
        'logout/',
        LogOutView.as_view(),
        name='logout_view'
    ),
]
