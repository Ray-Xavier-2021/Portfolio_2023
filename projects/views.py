from django.shortcuts import render

# Create your views here.
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets

class ProjectView(viewsets.ModelViewSet):
  # Get all Projects
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer


def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def projects(request):
  all_projects = Project.objects.all()
  return render(request, 'projects.html', {'projects': all_projects})

def detail(request, pk):
  project_detail = Project.objects.get(id=pk)
  return render(request, 'detail.html', {'project': project_detail})