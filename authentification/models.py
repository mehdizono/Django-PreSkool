import uuid
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_authorized = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # FIX: These must be strings to avoid clashing with Django's built-in User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
    )
    
    def __str__(self):
        return self.username


class PasswordResetRequest(models.Model):
    # FIX: Define the validity period (e.g., 1 hour)
    TOKEN_VALIDITY_PERIOD = timedelta(hours=1)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    
    # FIX: Pass uuid.uuid4 without the '()' so it generates a new token per instance
    token = models.CharField(max_length=255, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset token for {self.user.username}"
    
    def is_valid(self):
        return timezone.now() <= self.created_at + self.TOKEN_VALIDITY_PERIOD
    
    def send_reset_email(self):
        # Note: In production, don't hardcode localhost!
        reset_link = f"http://localhost:8000/reset-password/{self.token}"
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            # FIX: Typo from FORM to FROM, and added a fallback just in case
            getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'), 
            [self.email],
            fail_silently=False,
        )