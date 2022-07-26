# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from APIREST.models import Analytic
from django.http import FileResponse


def home(request):
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

    return render(request, 'knapsack/home.html')


def mentions(request):
    return render(request, 'knapsack/mentions.html')


def curriculum_vitae(request):
    # display cv
    filepath = os.path.join('media/pdf', 'cv_developer_mavamalonga.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
