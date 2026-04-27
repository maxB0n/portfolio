# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This maps the root URL (your homepage) to the index view
    path('', views.index, name='index'),
]