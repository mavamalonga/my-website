# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from APIREST.models import Analytic, CurriculumVitae
from django.http import FileResponse
from knapsack.forms import ContactForm
from django.core.mail import send_mail
from portfolio import settings


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

    form = ContactForm()

    # dowload cv
    curriculum_vitae = get_object_or_404(CurriculumVitae, pk=1)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            """
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            recipient = [settings.EMAIL_HOST_USER, ]
            send_mail(name, message, email_from, recipient
            """
            message = 'Le message a été envoyé avec succès !'
            context = {'curriculum_vitae': curriculum_vitae, 'form': form, 'message': message}
            return render(request, 'knapsack/home.html', context)

    context = {'curriculum_vitae': curriculum_vitae, 'form': form}
    return render(request, 'knapsack/home.html', context)


def mentions(request):
    return render(request, 'knapsack/mentions.html')


def curriculum_vitae(request):
    # display cv
    filepath = os.path.join('media/pdf', 'cv_developer_mavamalonga.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
