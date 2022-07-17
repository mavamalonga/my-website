# -*- coding: utf-8 -*-
from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', {'page': 'error'}, status=404)


def handler500(request):
    return render(request, '500.html', {'page': 'error'}, status=500)
