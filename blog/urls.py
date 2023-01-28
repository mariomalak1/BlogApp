from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostViewList.as_view(), name = "home-page"),
    path("about/", views.about, name = "about"),
    path("createPost/", views.PostCreateView.as_view(), name = "createPost"),
    path("postDetail/<int:pk>/", views.PostDetailView.as_view(), name = "postDetail"),
    path("PostEdit/<int:pk>/", views.PostUpdateView.as_view(), name = "PostUpdate"),
    path("postDelete/<int:pk>/", views.PostDeleteView.as_view(), name = "PostDelete"),
]
