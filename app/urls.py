
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.public,name='public'),
    path('index',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('user_list/',views.user_list,name='user_list'),

]