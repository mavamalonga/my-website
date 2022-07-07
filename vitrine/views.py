from multiprocessing import context
from django.shortcuts import render, redirect
from APIREST.models import CVPDF


def index(request):
    cv = CVPDF.objects.get(id=1)
    return render(request, 'vitrine/index.html', context={'cv': cv, 'page_name': 'dashboard'})

def mentions_legales(request):
    return render(request, 'vitrine/mentions.html', context)



