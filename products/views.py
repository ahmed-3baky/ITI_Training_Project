from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .project_data import PROJECTS , CONTACTS
from .models import Projects , Contacts

def all_projects(request)  : 
    projects= Projects.objects.all()
    return render(request,"projects.html" , context = {"projects" : projects})

def all_contacts(request)  : 
    contacts= Contacts.objects.all()

    return render(request,"contacts.html" , context = {"contacts" : contacts })

def get_project(request , project_id) : 
    project = get_object_or_404(Projects, id=project_id)
    return render(request, 'info.html', context={"project": project})

def get_contact(request , contact_id) : 
    contact = get_object_or_404(Contacts, id=contact_id)
    return render(request, 'info_contact.html', context={"contact": contact})

def get_project_contacts(request , project_id ) : 
    project = get_object_or_404(Projects, id=project_id)
    return render(request,"contacts.html" , context = {"contacts" : project.contacts.all()})

def deleteproject(request ,project_id ) : 
    project = get_object_or_404(Projects, id=project_id)
    project.delete()
    project_url = reverse('projects')
    return redirect(project_url)

def load_projects(request = 0) : 
    for i in PROJECTS :  
        new_project = Projects(name = i["name"] ,  description = i["description"] ,created_date = i["created_date"] 
                               , technology = i["technology"] , thumbnail = i["thumbnail"])
        new_project.save()

def load_contacts(request = 0) : 
    for i in CONTACTS :  
        new_contact = Contacts(id = i["id"],name = i["name"] , email = i["email"] , phone  = i["phone"]  , project_id = i["project_id"])
        new_contact.save()


def get_category(request, category_name):
    category_product = Projects.objects.filter(name=category_name).first()

    return render(request, 'projects.html',
                  context={"projects": category_product.products.all(), "title": f"{category_name} projects".capitalize()})
