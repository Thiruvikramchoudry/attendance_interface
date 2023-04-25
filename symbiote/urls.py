from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.main, name="home"),
    path('login_admin', views.login, name="login_admin"),
    # path('sample',views.sample,name="sample"),
    # path('clear_data',views.clear,name="clear_data"),
    path('employee_details', views.employee_detail, name="employee_details"),
    path('attendance_status', views.attendance_status, name="attendance_status"),
    path('add_employee', views.add_employee, name="add_employee"),
    path('imagecreation' , views.imagecreation, name='imagecreation'),
    # path('save_data',views.save_excel,name="save_data"),
    # path('save_clean',views.save_clear,name="save_clean"),
    path('download_stats', views.download_stats, name="download_stats"),
    path('login2', views.login2, name="login2"),
    path('logout', views.logout, name="logout"),
    path('login_supervisor', views.login_supervisor, name="login_supervisor"),
    path('admin_page', views.admin_page, name="admin_page"),
    path('supervisor_page', views.main, name="supervisor_page"),
    path('project_details', views.project_details, name="project_details"),
    path('employee_detail_all', views.employee_detail_all, name="employee_detail_all"),
    path('new_project', views.new_project, name="new_project"),
    path('video_feed', views.video_feed, name='video_feed'),
    path('stop_streaming', views.stop_streaming, name='stop_streaming'),
    path('uncapture', views.uncapture, name='uncapture'),
    path('video_feed1', views.video_feed1, name='video_feed1'),
    path('stop_streaming1', views.stop_streaming1, name='stop_streaming1'),
    path('uncapture1', views.uncapture1, name='uncapture1'),
    path('uncapture', views.uncapture, name='uncapture'),
    path('add_supervisor',views.add_supervisor,name='add_supervisor'),
    path('morning_update',views.morning_update,name="morning_update"),
    path('closing_update',views.closing_update,name="closing_update"),
    path('clear_project',views.clear_project,name="clear_project"),


]
