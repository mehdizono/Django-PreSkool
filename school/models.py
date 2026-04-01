import uuid

from django.db import models

from Home import settings

# Create your models here.
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

class Department(models.Model):
    department_id = models.CharField(max_length=50, unique=True, verbose_name="Department ID")
    name = models.CharField(max_length=100, verbose_name="Department Name")
    head_of_department = models.CharField(max_length=100, verbose_name="Head of Department")
    start_date = models.DateField(verbose_name="Department Start Date")
    no_of_students = models.IntegerField(verbose_name="No of Students", default=0)

    def __str__(self):
        return self.name
    
class Holiday(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la fête")
    holiday_date = models.DateField(verbose_name="Date du jour férié")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return f"{self.name} ({self.holiday_date})"