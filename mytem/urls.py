from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('accounts/', include('django.contrib.auth.urls')),
   
    path('accounts/', include('accounts.urls')),
    
    path('', include('website.urls')),

    path('login', include('accounts.urls')),
    path('login', include('website.urls')),
]
