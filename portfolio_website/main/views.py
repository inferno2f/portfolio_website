from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html',)

def experience(request):
    return render(request, 'main/experience.html')