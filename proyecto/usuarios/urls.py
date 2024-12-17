from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),    
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('recuperar_password/', views.recuperar_password, name='recuperar_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = 'usuarios/recuperar_password.html',
        email_template_name = 'usuarios/email_recuperacion.html',
        subject_template_name = 'usuarios/email_subject.txt',
        success_url = '/password_reset/don/'), 
        name='password_reset'
        ),
]   
