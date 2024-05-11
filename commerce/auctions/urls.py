from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("active_listing", views.active_listing, name="active_listing"),
    path("auction_view/<int:pk>", views.auction_view, name="auction_view"),
    path("categories", views.categories, name="categories"),
    path("category_listing/<str:cat>", views.category_listing, name="category_listing"),
    path("close_auction/<int:pk>", views.close_auction, name="close_auction"),
    path("wishlist/<int:pk>", views.wishlist, name="wishlist"),
    path("bookmarks", views.bookmarks, name="bookmarks"),
]
