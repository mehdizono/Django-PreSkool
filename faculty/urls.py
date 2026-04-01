from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    #teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/edit/<str:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<str:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('teachers/<str:teacher_id>/', views.view_teacher, name='view_teacher'),

    #departement
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('departments/delete/<int:pk>/', views.delete_department, name='delete_department'),

        #matières
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('subjects/edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<int:pk>/', views.delete_subject, name='delete_subject'),

    # Holidays
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('holidays/add/', views.add_holiday, name='add_holiday'),
    path('holidays/delete/<int:pk>/', views.delete_holiday, name='delete_holiday'),

    # Timetable
    path('timetable/', views.timetable, name='timetable'),
    path('timetable/add/', views.add_timetable, name='add_timetable'),
    path('timetable/delete/<int:pk>/', views.delete_timetable, name='delete_timetable'),

    # ─── Examens et Résultats ───
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.add_exam, name='add_exam'),
    path('results/', views.result_list, name='result_list'),
    path('results/add/', views.add_result, name='add_result'),




]