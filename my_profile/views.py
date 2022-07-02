from multiprocessing import context
from django.shortcuts import render
from APIREST.models import Project

def home(request):
    projects = Project.objects.all()
    print(projects)
    for project in projects:
        print(project.badges)
        print(project.image.image.url)
    context = {'projects': projects}
    return render(request, 'my_profile/home.html', context)