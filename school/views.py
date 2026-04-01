from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Notification
from django.http import HttpResponseForbidden
from .models import Department
from django.contrib import messages
from .models import Holiday 


# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html")



def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()


from .models import Department 
from django.shortcuts import render, redirect
from django.contrib import messages

def add_department(request):
    if request.method == 'POST':
        dept_id = request.POST.get('department_id')
        name = request.POST.get('name')
        head = request.POST.get('head_of_department')
        start_date = request.POST.get('start_date')
        students = request.POST.get('no_of_students')

        Department.objects.create(
            department_id=dept_id,
            name=name,
            head_of_department=head,
            start_date=start_date,
            no_of_students=students
        )
        messages.success(request, 'Département ajouté avec succès !')
        
      
        return redirect('department_list') 

    return render(request, 'school/add_department.html')

# NOUVELLE VUE : Pour afficher la liste
def department_list(request):
    # Récupérer tous les départements depuis la base de données
    departments = Department.objects.all()
    # Les envoyer au template HTML
    return render(request, 'school/department_list.html', {'departments': departments})



def holiday_list(request):
    # On récupère tous les jours fériés, triés par date
    holidays = Holiday.objects.all().order_by('holiday_date')
    return render(request, 'school/holidays.html', {'holidays': holidays})