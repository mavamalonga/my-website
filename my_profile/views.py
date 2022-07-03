from multiprocessing import context
from django.shortcuts import render
from APIREST.models import Project

def home(request):
    projects = Project.objects.all()
    skills = skills.objects.filter()
    for project in projects:
        print(project.skills)
    context = {'projects': projects}
    return render(request, 'my_profile/home.html', context)