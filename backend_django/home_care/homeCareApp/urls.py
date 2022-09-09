from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('nuevoUsuario', views.nuevoUsuario, name='nuevoUsuario'),
    path('nuevoPersona', views.nuevoPersona, name='nuevoPersona'),
    path('nuevoPaciente', views.nuevoPaciente, name='nuevoPaciente'),
    path('nuevoMedico', views.nuevoMedico, name='nuevoMedico'),
    path('nuevoFamiliar', views.nuevoFamiliar, name='nuevoFamiliar'),
    path('getAllPacientes', views.getAllPacientes, name='getAllPacientes'),
    path('getOnePaciente/<int:id>', views.getOnePaciente, name='getOnePaciente'),
]
