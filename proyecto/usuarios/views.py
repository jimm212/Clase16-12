from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'La dirección de correo electrónico ya está registrada.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Te has registrado correctamente.')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden!')
            
    return render(request, 'usuarios/registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('/')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has Cerrado la sesión con éxito.')
    return redirect('login')

def recuperar_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name = 'usuarios/email_recuperacion.html',
                subject_template_name = 'usuarios/email_subject.txt'
                )
            messages.success(request, 'Se ha enviado un correo de recuperación de contraseña')
            return redirect('login')
        else:
            messages.error(request, 'Error al enviar el correo verifique la dirección ingresado')
    
    return render(request, 'usuarios/recuperar_password.html')
