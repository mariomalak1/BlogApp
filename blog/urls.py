from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name = "home-page"),
    path("about/", views.about, name = "about"),

]
