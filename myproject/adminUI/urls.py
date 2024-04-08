from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    #     path('adminhome/',views.adminhome,name='adminhome'),
    #     path('adminlogout/',views.adminlogout,name='adminlogout'),
]
