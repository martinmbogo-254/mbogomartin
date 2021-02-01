from django.shortcuts import render
from .models import Profile, Project, Skill


def home(request):
    projects= Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'folio/home.html', context)
