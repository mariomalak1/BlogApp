from django.urls import path
from .views import register, accountView, accountAnotherView
from django.contrib.auth import views as views_auth
# from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path("registration/", register, name= "registration"),
    path("login/", views_auth.LoginView.as_view(template_name = "user/login_page.html"), name = "login"),
    path("logout/", views_auth.LogoutView.as_view(), name = "logout"),
    path("account/", accountView, name = "account-view"),
    path("accountAnother/<int:pk>", accountAnotherView, name = "account-another"),

    path("passwordReset/",
         views_auth.PasswordResetView.as_view(template_name='user/password/password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         views_auth.PasswordResetDoneView.as_view(template_name='user/password/password_reset_done.html'),
         name='password_reset_done'),

    path("passwordReset/Confirm/<uidb64>/<token>",
    views_auth.PasswordResetConfirmView.as_view(template_name='user/password/password_reset_confirm.html'),
    name = "passwordResetConfirm"),
]
