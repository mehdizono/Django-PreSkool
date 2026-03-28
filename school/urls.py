from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # Change views.index to views.home_page
    path('', views.home_page, name='index'), 
]