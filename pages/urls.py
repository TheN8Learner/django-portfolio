from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('project_detail/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills'),
    path('contact/success', views.contact_success, name='contact_success')


]