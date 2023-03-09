
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login', views.login, name="login"),
    path('sample',views.sample,name="sample"),
    path('clear_data',views.clear,name="clear_data"),
    path('employee_details',views.employee_detail,name="employee_details"),



]
