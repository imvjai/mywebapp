# Create your views here.

from django.shortcuts import render
from .models import Project, Blog

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def contact(request):
    return render(request, 'contact.html')
