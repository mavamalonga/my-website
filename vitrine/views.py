from multiprocessing import context
from django.shortcuts import render, redirect
from APIREST.models import CVPDF
from vitrine.forms import CustomerForm


def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'vitrine/index.html', context={'form': form})

def mentions_legales(request):
    cv = CVPDF.objects.get(id=1)
    context = {'cv': cv}
    return render(request, 'vitrine/mentions.html', context)

def plan(request):
    return render(request, 'vitrine/plan.html')

