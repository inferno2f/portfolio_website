from .forms import ContactForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import message, send_mail, BadHeaderError
from .models import Experience


def index(request):
    return render(request, 'main/index.html',)


def experience(request):
    response = Experience.objects.all()
    form = {
        'jobs': response
    }
    return render(request, 'main/experience.html', form)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name': form.cleaned_data['name'], 
            'subject': form.cleaned_data['subject'], 
            'email': form.cleaned_data['email'], 
            'body':form.cleaned_data['body'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('main:index')
        
    form = ContactForm()
    return render(request, 'main/contact.html', {'form':form})
