from django.contrib import admin
from .models import *
# Register your models here.

class AdminEvents(admin.ModelAdmin):
    list_display = ("title",  "summary", "created_at")
    
class AdminNews(admin.ModelAdmin):
    list_display = ("title", "author", "summary", "created_at")  
    
class AdminContact(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "short_content") 
    

admin.site.register(Event, AdminEvents)
admin.site.register(New, AdminNews)
admin.site.register(Contact, AdminContact)