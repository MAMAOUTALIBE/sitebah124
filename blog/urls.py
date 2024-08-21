from django.urls import path
from .views import *

urlpatterns = [
    
    path('', dashboard, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('news/', news, name='news'),
    path('news/<int:id>/', new_detail, name='new_details'),
    path('events/<int:id>/', event_detail, name='event_details'),
]