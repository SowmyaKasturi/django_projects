from django.shortcuts import render
from projects.models import Project
# Create your views here.
def all_projects(request):
    project = Project.objects.all()
    return render(request, "projects/allprojects.html", {'project':project})

def project_detail(request, k):
    project = Project.objects.get(id=k)
    return render(request, "projects/projectdetail.html", {'project':project})


def blog(request):
    return render(request, "projects/blog.html")

def about_me(request):
    return render(request, "projects/about_me.html")