from django.shortcuts import render
from .models import Experience


def index(request):
    return render(request, 'main/index.html',)

def experience(request):
    response = Experience.objects.all()
    form = {
        'jobs': response
    }
    return render(request, 'main/experience.html', form)