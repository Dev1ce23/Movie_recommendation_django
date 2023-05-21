from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
  path('', views.starting_page, name="starting_page"),
  path('login/', views.loginView, name="login"),
  path('signup/', views.signup, name="signup"),
  path('home/', views.home, name="home"),
  path ('movie-search/', views.movieSearch, name="movie-search"),
  path('logout/',views.logoutPage, name="logout")
]