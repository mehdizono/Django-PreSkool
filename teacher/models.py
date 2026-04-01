from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Add any other fields you need for a teacher
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"