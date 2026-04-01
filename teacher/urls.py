# teacher/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add/', views.teacher_create, name='teacher_create'),
    path('edit/<int:pk>/', views.teacher_update, name='teacher_update'),
    path('delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
]