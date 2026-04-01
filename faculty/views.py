# faculty/views.py
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Teacher, Department, Subject, Holiday, Exam, ExamResult, Timetable
from student.models import Student
from django.contrib.auth.decorators import login_required, user_passes_test
#from django.http import HttpResponse

# Create your views here.
def is_admin(user):
    return user.is_authenticated and getattr(user, 'is_admin', False)
def is_teacher_or_admin(user):
    return user.is_authenticated and (getattr(user, 'is_teacher', False) or getattr(user, 'is_admin', False))

def index(request):
    # return HttpResponse('First test')  <- l'ancienne version
    #return render(request, 'Home/index.html')
    return render(request, 'authentification/login.html')
def dashboard(request):
    return render (request, 'students/student-dashboard.html')

def teacher_list(request):
    # 1. On récupère tous les enseignants de la base de données
    teachers = Teacher.objects.all()
    
    # 2. On les envoie (contexte) à un template HTML qu'on créera juste après
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

@user_passes_test(is_admin)
def add_teacher(request):
    # Si le formulaire a été soumis (clic sur le bouton Enregistrer)
    if request.method == 'POST':
        # 1. On récupère toutes les données tapées dans les champs 'name' du HTML
        teacher_id = request.POST.get('teacher_id')
        
        # Vérification si cet ID existe déjà pour éviter l'erreur d'intégrité (UNIQUE constraint failed)
        if Teacher.objects.filter(teacher_id=teacher_id).exists():
            messages.error(request, f"Un enseignant avec l'ID '{teacher_id}' existe déjà. Veuillez utiliser un identifiant unique.")
            return redirect('add_teacher')
            
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        
        # ATTENTION : Pour les fichiers/images, on utilise request.FILES, pas request.POST
        image = request.FILES.get('image')

        # 2. On crée la nouvelle ligne dans la base de données
        Teacher.objects.create(
            teacher_id=teacher_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            joining_date=joining_date,
            mobile_number=mobile_number,
            address=address,
            experience=experience,
            image=image
        )

        # 3. On prépare un message de succès
        messages.success(request, 'L\'enseignant a été ajouté avec succès !')
        
        # 4. On redirige l'utilisateur vers la page qui liste les profs
        return redirect('teacher_list')
    
    # Si ce n'est pas un POST (ex: on vient juste d'ouvrir la page), on affiche le HTML
    return render(request, 'teachers/add-teacher.html')

@user_passes_test(is_admin)
def delete_teacher(request, teacher_id):
    # 1. On récupère le prof
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    
    # 2. On le supprime de la base de données
    teacher.delete()
    
    # 3. On affiche un message et on redirige
    messages.success(request, 'Enseignant supprimé avec succès !')
    return redirect('teacher_list')


@user_passes_test(is_admin)
def edit_teacher(request, teacher_id):
    # 1. On récupère le prof spécifique grâce à son ID
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

    if request.method == 'POST':
        # 2. On met à jour les champs avec les nouvelles données du formulaire
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.address = request.POST.get('address')
        teacher.experience = request.POST.get('experience')
        
        # On vérifie s'il a uploadé une nouvelle image, sinon on garde l'ancienne
        if request.FILES.get('image'):
            teacher.image = request.FILES.get('image')
        
        # 3. On sauvegarde les modifications
        teacher.save()
        messages.success(request, 'Enseignant mis à jour avec succès !')
        return redirect('teacher_list')

    # Si c'est un GET, on affiche la page en lui envoyant les données du prof
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})


# --- VUE : Voir les détails d'un enseignant ---
def view_teacher(request, teacher_id):
    # 1. On récupère le prof grâce à son ID
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    
    # 2. On envoie les données à la page de profil
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})

# Liste des départements
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

# Ajouter un département 
@user_passes_test(is_admin)
def add_department(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        head_teacher_id = request.POST.get('head_teacher')
        teacher_ids = request.POST.getlist('teachers')

        head_teacher = Teacher.objects.get(id=head_teacher_id) if head_teacher_id else None

        department = Department.objects.create(
            name=name,
            description=description,
            head_teacher=head_teacher
        )
        department.teachers.set(teacher_ids)
        department.save()

        messages.success(request, 'Département ajouté avec succès !')
        return redirect('department_list')

    return render(request, 'departments/add-department.html', {'teachers': teachers})

#Modifier un département
@user_passes_test(is_admin)
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        head_teacher_id = request.POST.get('head_teacher')
        teacher_ids = request.POST.getlist('teachers')

        department.head_teacher = Teacher.objects.get(id=head_teacher_id) if head_teacher_id else None
        department.teachers.set(teacher_ids)
        department.save()

        messages.success(request, 'Département mis à jour avec succès !')
        return redirect('department_list')

    return render(request, 'departments/edit-department.html', {
        'department': department,
        'teachers': teachers
    })

# Supprimer un département
@user_passes_test(is_admin)
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    messages.success(request, 'Département supprimé avec succès !')
    return redirect('department_list')
# ─── MATIÈRES ───────────────────────────────────────

def subject_list(request):
    subjects = Subject.objects.select_related('department', 'teacher').all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})

@user_passes_test(is_teacher_or_admin)
def add_subject(request):
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        description = request.POST.get('description')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')

        Subject.objects.create(
            name=name,
            code=code,
            description=description,
            department=Department.objects.get(id=department_id) if department_id else None,
            teacher=Teacher.objects.get(id=teacher_id) if teacher_id else None,
        )
        messages.success(request, 'Matière ajoutée avec succès !')
        return redirect('subject_list')

    return render(request, 'subjects/add-subject.html', {
        'departments': departments,
        'teachers': teachers
    })

@user_passes_test(is_teacher_or_admin)
def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        subject.description = request.POST.get('description')
        dep_id = request.POST.get('department')
        tea_id = request.POST.get('teacher')
        subject.department = Department.objects.get(id=dep_id) if dep_id else None
        subject.teacher = Teacher.objects.get(id=tea_id) if tea_id else None
        subject.save()
        messages.success(request, 'Matière mise à jour !')
        return redirect('subject_list')

    return render(request, 'subjects/edit-subject.html', {
        'subject': subject,
        'departments': departments,
        'teachers': teachers
    })

@user_passes_test(is_teacher_or_admin)
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, 'Matière supprimée !')
    return redirect('subject_list')

# --- Holidays ---
def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'holidays/holidays.html', {'holidays': holidays})

@user_passes_test(is_admin)
def add_holiday(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        description = request.POST.get('description')
        Holiday.objects.create(name=name, date=date, description=description)
        messages.success(request, 'Jour férié ajouté avec succès !')
        return redirect('holiday_list')
    return render(request, 'holidays/add-holiday.html')

@user_passes_test(is_admin)
def delete_holiday(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    holiday.delete()
    messages.success(request, 'Jour férié supprimé !')
    return redirect('holiday_list')

# --- Time Table ---
def timetable(request):
    entries = Timetable.objects.select_related('subject', 'teacher').all()
    
    # Organiser les données par jour pour faciliter l'affichage en grille
    timetable_data = {i: [] for i in range(1, 7)}
    for entry in entries:
        timetable_data[entry.day].append(entry)
        
    context = {
        'timetable_data': timetable_data,
        'days_names': {
            1: 'Lundi', 2: 'Mardi', 3: 'Mercredi', 
            4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi'
        }
    }
    return render(request, 'timetable/timetable.html', context)

@user_passes_test(is_teacher_or_admin)
def add_timetable(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    days = Timetable.DAYS_OF_WEEK
    
    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        room = request.POST.get('room')

        Timetable.objects.create(
            subject_id=subject_id,
            teacher_id=teacher_id,
            day=day,
            start_time=start_time,
            end_time=end_time,
            room=room
        )
        messages.success(request, 'Créneau ajouté avec succès !')
        return redirect('timetable')

    return render(request, 'timetable/add-timetable.html', {
        'subjects': subjects,
        'teachers': teachers,
        'days': days
    })

@user_passes_test(is_teacher_or_admin)
def delete_timetable(request, pk):
    entry = get_object_or_404(Timetable, pk=pk)
    entry.delete()
    messages.success(request, 'Créneau supprimé avec succès !')
    return redirect('timetable')

# ─── EXAMENS : Planification ───────────────────────────────────────

def exam_list(request):
    exams = Exam.objects.select_related('subject').all()
    return render(request, 'exams/exam_list.html', {'exams': exams})

@user_passes_test(is_teacher_or_admin)
def add_exam(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        exam_name = request.POST.get('exam_name')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        Exam.objects.create(
            exam_name=exam_name,
            subject_id=subject_id, # Remarquez comment on utilise l'ID directement
            exam_date=exam_date,
            start_time=start_time,
            end_time=end_time
        )
        messages.success(request, 'Examen planifié avec succès !')
        return redirect('exam_list')
    return render(request, 'exams/add_exam.html', {'subjects': subjects})

# ─── RÉSULTATS : Saisie des notes ───────────────────────────────────

def result_list(request):
    results = ExamResult.objects.select_related('exam', 'student').all()
    return render(request, 'exams/result_list.html', {'results': results})

@user_passes_test(is_teacher_or_admin)
def add_result(request):
    exams = Exam.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        exam_id = request.POST.get('exam')
        student_id = request.POST.get('student')
        marks = request.POST.get('marks')
        total_marks = request.POST.get('total_marks', 20.00) # 20 par défaut si non fourni
        comments = request.POST.get('comments')

        ExamResult.objects.create(
            exam_id=exam_id,
            student_id=student_id,
            marks_obtained=marks,
            total_marks=total_marks,
            comments=comments
        )
        messages.success(request, 'Résultat saisi avec succès !')
        return redirect('result_list')
    return render(request, 'exams/add_result.html', {'exams': exams, 'students': students})
