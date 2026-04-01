
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Teacher
from .forms import TeacherForm

# 1. READ: Display a list of all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

# 2. CREATE: Add a new teacher
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher added successfully!')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    
    return render(request, 'teacher/teacher_form.html', {'form': form, 'title': 'Add Teacher'})

# 3. UPDATE: Edit an existing teacher
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully!')
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
        
    return render(request, 'teacher/teacher_form.html', {'form': form, 'title': 'Edit Teacher'})

# 4. DELETE: Remove a teacher
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully!')
        return redirect('teacher_list')
        
    return render(request, 'teacher/teacher_confirm_delete.html', {'teacher': teacher})