from django.db import models
from django.conf import settings

class Teacher(models.Model):
   
    
    teacher_id = models.CharField(max_length=20, unique=True, verbose_name="ID Enseignant")
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    gender = models.CharField(max_length=10, choices=[('Male', 'Masculin'), ('Female', 'Féminin')], verbose_name="Genre")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    joining_date = models.DateField(verbose_name="Date d'embauche")
    mobile_number = models.CharField(max_length=15, verbose_name="Numéro de téléphone")
    address = models.TextField(blank=True, null=True, verbose_name="Adresse")
    experience = models.CharField(max_length=50, blank=True, null=True, verbose_name="Expérience")
    image = models.ImageField(upload_to='teachers/', blank=True, null=True, verbose_name="Photo de profil")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#classeDepartement    
    
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du département")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    head_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments',
        verbose_name="Responsable (Enseignant)"
    )
    teachers = models.ManyToManyField(
        Teacher,
        blank=True,
        related_name='departments',
        verbose_name="Enseignants"
    )

    def __str__(self):
        return self.name


# Ligne 44 et suivantes — après class Department
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la matière")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    
    # Lien avec Department (une matière appartient à un département)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subjects',
        verbose_name="Département"
    )
    
    # Lien avec Teacher (un enseignant enseigne cette matière)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subjects',
        verbose_name="Enseignant"
    )

    def __str__(self):
        return self.name
    
#jour feries (holidays)
class Holiday(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du jour férié")
    date = models.DateField(verbose_name="Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.name} ({self.date})"
    
# ─── EXAMENS & RÉSULTATS ────────────────────────────────

class Exam(models.Model):
    exam_name = models.CharField(max_length=100, verbose_name="Nom de l'examen (ex: Contrôle Continu 1)")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Matière")
    exam_date = models.DateField(verbose_name="Date de l'examen")
    start_time = models.TimeField(verbose_name="Heure de début")
    end_time = models.TimeField(verbose_name="Heure de fin")

    def __str__(self):
        return f"{self.exam_name} - {self.subject.name}"

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="Examen")
    # On utilise 'student.Student' sous forme de texte pour éviter les erreurs d'importation circulaires
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, verbose_name="Étudiant")
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Note obtenue")
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=20.00, verbose_name="Note sur (ex: 20)")
    comments = models.TextField(blank=True, null=True, verbose_name="Appréciation")

    def __str__(self):
        return f"Résultat de {self.student.first_name} pour {self.exam.exam_name}"

class Timetable(models.Model):
    DAYS_OF_WEEK = [
        (1, 'Lundi'),
        (2, 'Mardi'),
        (3, 'Mercredi'),
        (4, 'Jeudi'),
        (5, 'Vendredi'),
        (6, 'Samedi'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Matière")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Enseignant")
    day = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name="Jour de la semaine")
    start_time = models.TimeField(verbose_name="Heure de début")
    end_time = models.TimeField(verbose_name="Heure de fin")
    room = models.CharField(max_length=50, blank=True, null=True, verbose_name="Salle")

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.get_day_display()} - {self.subject.name} ({self.start_time})"
