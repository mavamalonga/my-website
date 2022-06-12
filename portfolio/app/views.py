from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def blogs(request):
    return render(request, 'app/blogs.html')
