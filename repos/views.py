from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ProjectModelForm
from products.models import Projects
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def create(request):
    project_form = ProjectModelForm()

    if request.method == "POST":
        print(request.FILES.get("thumbnail"))
        form = ProjectModelForm(request.POST, request.FILES)
        if form.is_valid():form.save()
    return render(request, "form.html", context={"form": project_form, "form_title": "Create New Product"})

@login_required

def edit(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == "GET":
        project_form = ProjectModelForm(instance=project)
        return render(request, "form.html", context={"form": project_form, "form_title": "Edit Product"})
    else:
        project_form = ProjectModelForm(request.POST, instance=project)
        if project_form.is_valid():project_form.save()
        project_url = project.get_project_url()
        return redirect(project_url)

class ProjectCreateView(CreateView , LoginRequiredMixin):
    model = Projects
    form_class = ProjectModelForm
    template_name = 'form.html'

    def form_valid(self, form):
        new_project = form.save()
        return redirect(new_project.get_project_url())