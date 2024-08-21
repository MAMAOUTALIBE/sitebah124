from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail




# Create your views here.
def dashboard(request):
    
    news = New.objects.all().order_by('-created_at')[0:6]
    
    return render(request, 'index.html', context={'news' : news})
    
def contact(request):
    
    message = ''
    
    if request.method == 'POST':
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        telephone = request.POST.get('telephone')
        msg = request.POST.get('msg')
        email = request.POST.get('email')
        
        contact = Contact.objects.create(
            first_name = fname,
            last_name = lname,
            phone = telephone,
            email = email,
            message = msg,
        )
        
        contact.save()
        
        #print(fname)
        
        message = "Message envoyé avec succèss"
        link = 'Cliquez sur ce lien pour voir le message : https://rtk-agency-v1-0.onrender.com/admin/'
        mailContent = f"Bonjour,\n\n{fname} {lname} vient de vous envoyer un message via le site web.\n\n{link}"
        
        send_mail(
            "Notification - RTK Agency",
            mailContent,
            None,
            ["ourobodiabdourakibou@gmail.com"],
            fail_silently=False,
        )
       
        
    context = {
        'message' : message
    }
    
    return render(request, 'contact.html', context=context)

def about(request):
    
    events = Event.objects.all().order_by('-created_at')[0:6]
    
    return render(request, 'about.html', context={'events': events})


def events(request):
    
    events_list = Event.objects.all().order_by('-created_at')
    
    page = request.GET.get('page', 1)
    
    paginator = Paginator(events_list, 6)
    
    try:
        events = paginator.page(page)
        
    except PageNotAnInteger:
        events = paginator.page(1)
        
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    context = {
        'events' : events
    }
    
    return render(request, 'event.html', context=context)


def news(request):
    
    news_list = New.objects.all().order_by('-created_at')
    
    page = request.GET.get('page', 1)
    
    paginator = Paginator(news_list, 6)
    
    try:
        news = paginator.page(page)
        
    except PageNotAnInteger:
        news = paginator.page(1)
        
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
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


def event_detail(request, id):
    
    event = Event.objects.get(id=id)
    
    context = {
        'event' : event
    }
    
    return render(request, 'events-details.html', context=context)


