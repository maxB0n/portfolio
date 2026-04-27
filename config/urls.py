# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This routes to the default Django admin panel
    path('admin/', admin.site.urls),
    
    # This hands off all other traffic to your portfolio app
    path('', include('portfolio.urls')),
]