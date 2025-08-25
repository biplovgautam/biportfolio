from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('projects/', views.projects, name="projects"),
    path('project/<int:project_id>/', views.project_detail, name="project_detail"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact/', views.contact, name="contact"),
    path('sync-medium-blogs/', views.sync_medium_blogs, name="sync_medium_blogs"),
]