
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('login', views.login, name="login"),
    path('sample',views.sample,name="sample"),
    path('clear_data',views.clear,name="clear_data"),
    path('employee_details',views.employee_detail,name="employee_details"),
    path('attendance_status',views.attendance_status,name="attendance_status"),
    path('add_employee',views.add_employee,name="add_employee"),
    path('save_data',views.save_excel,name="save_data"),
    path('save_clean',views.save_clear,name="save_clean"),
    path('download_stats',views.download_stats,name="download_stats"),

]
