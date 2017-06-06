 
# Create your views here.


from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.shortcuts import render, get_object_or_404


urlpatterns = [
    url(r'^$', views.statistics, name='statistics'), 
    
]
