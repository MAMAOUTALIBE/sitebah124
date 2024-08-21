
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

admin.site.site_header = 'RTK Agency Blog Dashboard'
admin.site.site_title = 'RTK Agency Blog Admin'
admin.site.index_title= 'RTK Agency Blog Dashboard Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
