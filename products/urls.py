"""
URL configuration for portifolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import * 
urlpatterns = [
    path('', all_projects, name="projects"),
    path('contacts', all_contacts, name="contacts"),
    path('<int:project_id>', get_project, name="project"),  
    path('<int:project_id>/delete', deleteproject, name="delete_project"),  
    path('load', load_projects),
    path('loads', load_contacts),
    path('<int:project_id>/contacts', get_project_contacts, name="project_contacts"),
    path('contacts/<int:contact_id>', get_contact, name="contact")


]
