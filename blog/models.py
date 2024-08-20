from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/events/', default='images/events/02.png')
    summary = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.created_at}"
    
    
class New(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/news/', default='images/news/03.png')
    summary = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.author} - {self.created_at}"
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"