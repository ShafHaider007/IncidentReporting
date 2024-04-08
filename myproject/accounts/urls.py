
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path('checkreport/', views.checkreport, name='checkreport'),
    
    
    
]
