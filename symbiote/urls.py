
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login', views.login, name="login"),


]
