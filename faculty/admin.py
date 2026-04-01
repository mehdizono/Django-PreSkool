from django.contrib import admin
from .models import Teacher, Department, Holiday, Subject, Timetable

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'first_name', 'last_name', 'gender', 'mobile_number')
    search_fields = ('teacher_id', 'first_name', 'last_name')
    list_filter = ('gender',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_teacher')
    search_fields = ('name',)
    filter_horizontal = ('teachers',)

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    search_fields = ('name',)
    list_filter = ('date',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'teacher')
    search_fields = ('name', 'code')

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'subject', 'teacher', 'room')
    list_filter = ('day', 'teacher')
    ordering = ('day', 'start_time')
