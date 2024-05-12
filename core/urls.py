from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings 
from appd import views

urlpatterns = [ 
	path('admin/', admin.site.urls), # URL pattern for the admin interface 
    path('main',views.mainpage),
	path('', include('app.urls')),
	path('', include('appd.urls')),
	path('', include('appbc.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serve media files during development 

	
