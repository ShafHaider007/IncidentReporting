from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("report/", views.report, name="report"),
    path("status/", views.status, name="status"),
    path('incident_list/', views.incident_list, name='incident_list'),
    path("check_status/", views.check_status, name="check_status"),
    path('get_incident_details/<int:report_id>/', views.get_incident_details, name='incident_details'),
    path('user_report_history/<str:user_name>/', views.user_report_history, name='user_report_history'),
    
]
