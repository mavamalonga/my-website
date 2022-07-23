# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import Http404
from APIREST.models import Project, Task, Badge, Analytic
from django.views.decorators.cache import cache_page
from django.http import FileResponse


@cache_page(60 * 15)
def index(request):
    # count visits
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if ip != os.getenv('MY_IP'):
        analytic = Analytic.objects.get(page_title='Home')
        analytic.visits = analytic.visits + 1
        analytic.save()

    # collect top projects objects
    my_objects = Project.objects.filter(title__in=['My-Portfolio', 'SoftDesk'])

    # return an error if there are no projects
    if not my_objects:
        raise Http404("Projects does not exist")

    # collects badges and tasks for each project
    projects = [{'project': project, 'badges': Badge.objects.filter(projects__id=project.id),
    'tasks': Task.objects.filter(projects__id=project.id)} for project in my_objects]

    return render(request, 'dashboard/index.html', {'projects': projects})


@cache_page(60 * 15)
def mentions_legales(request):
    return render(request, 'dashboard/dashboard.html')


@cache_page(60 * 15)
def curriculum_vitae(request):
    # display cv
    filepath = os.path.join('media/pdf', 'cv_developer_mavamalonga.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
