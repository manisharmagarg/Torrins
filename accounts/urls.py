from django.urls import path

from .views import (
    SignUpView,
    # EmailConformationView,
    LoginView,
    # PasswordResetApiView,
    LogOutView,
    # UserDetailApiView
)


urlpatterns = [
    path(
        'register/',
        SignUpView.as_view(),
        name='signup',
    ),
    # path(
    #     'email-conformation/<str:activation_key>/',
    #     EmailConformationView.as_view(),
    #     name='email_conformation'
    # ),
    path('login/', 
        LoginView.as_view(),
        name='login_view'
    ),
    # path(
    #     'change-password/',
    #     PasswordResetApiView.as_view(),
    #     name='change-password',
    # ),
    # path(
    # 	'user/',
    # 	UserDetailApiView.as_view(),
    #     name='user-detail',
    # ),
    path('logout/', 
        LogOutView.as_view()
    ),
]
