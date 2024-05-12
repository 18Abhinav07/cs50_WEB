from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("user_info/<int:pk>", views.user_info, name="user_info"),
    path("like/<int:pk>", views.like, name="like"),
    path("dislike/<int:pk>", views.dislike, name="dislike"),
    path("follow/<int:pk>",views.follow,name="follow"),
    path("unfollow/<int:pk>",views.unfollow,name="unfollow"),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    
]
