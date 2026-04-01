from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('dashboard/', views.dashboard, name='dashboard'), 
   path('notifications/mark-as-read/', views.mark_notification_as_read, name='mark_notifications_as_read'),
   path('notifications/clear-all/', views.clear_all_notification, name='clear_all_notifications'),
   path('add-department/', views.add_department, name='add_department'),
   path('departments/', views.department_list, name='department_list'),
   path('holidays/', views.holiday_list, name='holidays'),
]