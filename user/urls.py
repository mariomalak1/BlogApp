from django.urls import path
from .views import register, accountView, accountAnotherView
from django.contrib.auth import views as views_auth

urlpatterns = [
    path("registration/", register, name= "registration"),
    path("login/", views_auth.LoginView.as_view(template_name = "user/login_page.html"), name = "login"),
    path("logout/", views_auth.LogoutView.as_view(), name = "logout"),
    path("account/", accountView, name = "account-view"),
    path("accountAnother/<int:pk>", accountAnotherView, name = "account-another")
]
