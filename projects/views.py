# -*- coding: utf-8 -*-
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from APIREST.models import Project, Skill, Badge, CVPDF


def projects(request):
    # collect cv and top projects objects
    curriculum_vitae = get_object_or_404(CVPDF, pk=1)

    # My technological expertise
    techs = ['Python', 'Django', 'Flask', 'JavaScript', 'React', 'Node', 'Rust']

    queryset = Project.objects.all()

    # selects the projects of a technology
    if request.GET.get('filter') in techs:
        queryset = [project for project in Project.objects.all()
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
        'skills': Skill.objects.filter(projects__id=project.id)} for project in projects_of_page]

    context = {'projects': projects, 'projects_of_page': projects_of_page,
        'number_of_pages': number_of_pages, 'curriculum_vitae': curriculum_vitae}
    return render(request, 'projects/projects.html', context)
