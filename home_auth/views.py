from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .models import CustomUser
from .models import PasswordResetRequest

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        role = request.POST.get('role') # student, teacher ou admin

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé par un autre compte.")
            return render(request, 'authentification/register.html')


        user = CustomUser.objects.create_user( 
            username=email, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
            )
        
        if role == 'student': 
            user.is_student = True 
        elif role == 'teacher': 
            user.is_teacher = True 
        elif role == 'admin': 
            user.is_admin = True

        user.save() 
        login(request, user) 
        messages.success(request, 'Signup successful!') 
        return redirect('index') 
    return render(request, 'authentification/register.html')

def login_view(request): 
    if request.method == 'POST': 
        email = request.POST.get('email') 
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie !') 
            
            if getattr(user, 'is_admin', False): 
                return redirect('dashboard') 
            elif getattr(user, 'is_teacher', False): 
                return redirect('dashboard') 
            elif getattr(user, 'is_student', False):
                return redirect('dashboard')
            else:
                messages.error(request, 'Rôle utilisateur invalide') 
                return redirect('index')
        else:
            messages.error(request, 'Identifiants invalides') 

    return render(request, 'authentification/login.html')




def logout_view(request): 
    logout(request) 
    messages.success(request, 'You have been logged out.') 
    return redirect('index')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            reset_req = PasswordResetRequest.objects.create(user=user, email=email)
            reset_req.send_reset_email() 
            messages.success(request, 'Un lien de réinitialisation a été envoyé à votre email (visitez votre console terminal si vous êtes en local).')
            return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Aucun compte associé à cet email.')
            return redirect('forgot-password')
    return render(request, 'authentification/forgot-password.html')

def reset_password(request, token):
    try:
        reset_req = PasswordResetRequest.objects.get(token=token)
    except PasswordResetRequest.DoesNotExist:
        messages.error(request, 'Ce lien de réinitialisation est invalide.')
        return redirect('forgot-password')
        
    if not reset_req.is_valid():
        messages.error(request, 'Ce lien de réinitialisation a expiré.')
        return redirect('forgot-password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password and new_password == confirm_password:
            user = reset_req.user
            user.set_password(new_password)
            user.save()
            reset_req.delete() 
            messages.success(request, 'Votre mot de passe a été réinitialisé ! Connectez-vous.')
            return redirect('login')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas.')

    return render(request, 'authentification/reset_password.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Simple validation
        if not first_name or not last_name or not email:
            messages.error(request, "Tous les champs sont obligatoires.")
        else:
            # Check if email is already taken by another user
            if CustomUser.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                messages.error(request, "Cet email est déjà lié à un autre compte.")
            else:
                user = request.user
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = email # Synchronizing username with email as done in signup
                user.save()
                messages.success(request, "Profil mis à jour avec succès !")
                return redirect('profile')

    return render(request, 'authentification/profile.html')
