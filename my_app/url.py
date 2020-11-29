from django.urls import path
from my_app import views

urlpatterns = [
    path("",views.home , name = "home"),
    path("store",views.store , name = "store"),
    path("product=<slug>",views.details , name = "details"),
    path("products=<typer>" , views.products , name = "products"),
    path("register" , views.accounts , name = "accounts"),
    path("logme" , views.logginner , name = "login"),
    path("rating" , views.user_rating , name = "rating"),
    path("logout" , views.logouter , name = "logout"),
    path("login" , views.accounts , name = "accounts")
]