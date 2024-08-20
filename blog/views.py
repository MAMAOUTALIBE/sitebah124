from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard(request):
    
    return render(request, 'index.html', context={})
    
def contact(request):
    context = {
        'message' : "Message envoyé avec succès"
    }
    return render(request, 'contact.html', context=context)

def about(request):
    
    return render(request, 'about.html', context={})


def events(request):
    
    events = Event.objects.all()
    
    context = {
        'events' : events
    }
    
    return render(request, 'event.html', context=context)


def news(request):
    
    news = New.objects.all()
    
    context = {
        'news' : news
    }
    
    return render(request, 'news.html', context=context)


def new_detail(request, id):
    
    new = New.objects.get(id=id)
    
    context = {
        'new' : new
    }
    
    return render(request, 'news-details.html', context=context)