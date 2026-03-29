from urllib import request
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

import student
from .models import Student, Parent

# Create your views here.
def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'student_list': student_list
    }
    return render(request, 'students/students.html', context)

def add_student(request):
    if request.method == 'POST':
        # Get all the text data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        
        # Get the image file
        student_image = request.FILES.get('student_image')

        # Get parent data
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # Save parent information
        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )

        # Save student information
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender=gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            joining_date=joining_date,
            mobile_number=mobile_number,
            admission_number=admission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )
        
        messages.success(request, 'Student added successfully!')
        
        # It's good practice to redirect after a successful POST to prevent duplicate submissions
        return redirect('add_student') 

    # If it's a GET request (meaning they just clicked the link to view the page), show the empty form
    return render(request, 'students/add-student.html')


def edit_student(request, student_id):
    # 1. Grab the specific student and parent instances (lowercase)
    student = get_object_or_404(Student, student_id=student_id)
    parent = student.parent if hasattr(student, 'parent') else None

    if request.method == 'POST':
        # 2. Update Student fields (lowercase 'student', NO trailing commas!)
        Student.first_name = request.POST.get('first_name')
        Student.last_name = request.POST.get('last_name')
        Student.student_id = request.POST.get('student_id')
        Student.gender = request.POST.get('gender')
        Student.date_of_birth = request.POST.get('date_of_birth')
        Student.student_class = request.POST.get('student_class')
        Student.joining_date = request.POST.get('joining_date')
        Student.mobile_number = request.POST.get('mobile_number')
        Student.admission_number = request.POST.get('admission_number')
        Student.section = request.POST.get('section')
        
        # 3. Handle the image safely (only update if a new file was uploaded)
        student_image = request.FILES.get('student_image')
        if student_image:
            student.student_image = student_image

        # 4. Update Parent fields (lowercase 'parent')
        if parent:
            Parent.father_name = request.POST.get('father_name')
            Parent.father_occupation = request.POST.get('father_occupation')
            Parent.father_mobile = request.POST.get('father_mobile')
            Parent.father_email = request.POST.get('father_email')
            Parent.mother_name = request.POST.get('mother_name')
            Parent.mother_occupation = request.POST.get('mother_occupation')
            Parent.mother_mobile = request.POST.get('mother_mobile')
            Parent.mother_email = request.POST.get('mother_email')
            Parent.present_address = request.POST.get('present_address')
            Parent.permanent_address = request.POST.get('permanent_address')
            parent.save() # Save the parent instance

        # 5. Save the student instance
        student.save()

        # Optional: Add a success message
        messages.success(request, 'Student updated successfully!')
        
        # 6. Redirect to the list view instead of rendering just a string
        return redirect("student_list")

    # 7. If GET request, render the edit page and pass the variables (lowercase)
    context = {
        'student': student,
        'parent': parent
    }
    return render(request, 'students/edit-student.html', context)
def view_student(request, student_id):
    # 1. Fetch the specific student from the database
    student = get_object_or_404(Student, student_id=student_id)
    
    # 2. Put the student into the context dictionary
    context = {
        'student': student 
    }
    
    # 3. Pass the context to the template
    return render(request, 'students/student-details.html', context)
    return render(request, 'students/student-details.html')

def delete_student(request, slug):
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        Student.name = f"{student.first_name} {student.last_name}"
        student.delete()
    return redirect('student_list')
    return HttpResponseForbidden()