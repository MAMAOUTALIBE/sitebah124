
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

admin.site.site_header = 'Blog Dasboard'
admin.site.site_title = 'Blog Admin'
admin.site.index_title= 'Blog Dashboard Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
