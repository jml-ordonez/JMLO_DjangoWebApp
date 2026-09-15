from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('registration/', include('registration.urls')),  
    path('api/', include('registration.api_urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]