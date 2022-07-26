# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from APIREST.models import Project, Task, Badge, Analytic, CurriculumVitae
from django.views.decorators.cache import cache_page
from django.http import FileResponse
from django.core.paginator import Paginator


#@cache_page(60 * 15)
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


#@cache_page(60 * 15)
def mentions_legales(request):
    return render(request, 'dashboard/dashboard.html')


#@cache_page(60 * 15)
def curriculum_vitae(request):
    # display cv
    filepath = os.path.join('media/pdf', 'cv_developer_mavamalonga.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


#@cache_page(60 * 15)
def projects(request):
    # collect cv and top projects objects
    curriculum_vitae = get_object_or_404(CurriculumVitae, pk=1)

    # My technological expertise
    techs = ['Python', 'Django', 'Flask', 'JavaScript', 'React', 'Node', 'Rust']

    queryset = Project.objects.all()

    # selects the projects of a technology
    if request.GET.get('filter') in techs:
        queryset = [project for project in Project.objects.get_queryset().order_by('id')
            if get_object_or_404(Badge, name=request.GET.get('filter')) in
            Badge.objects.filter(projects__id=project.id)]

    # Set up Paginator
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    projects_of_page = paginator.get_page(page)
    number_of_pages = "a" * projects_of_page.paginator.num_pages

    # filter badges and project tasks
    projects = [
        {'project': project, 'badges': Badge.objects.filter(projects__id=project.id),
        'tasks': Task.objects.filter(projects__id=project.id)} for project in projects_of_page]

    context = {'projects': projects, 'projects_of_page': projects_of_page,
        'number_of_pages': number_of_pages, 'curriculum_vitae': curriculum_vitae}
    return render(request, 'projects/projects.html', context)

