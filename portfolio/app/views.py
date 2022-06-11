from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def blog(request):
    return render(request, 'app/blog.html')
