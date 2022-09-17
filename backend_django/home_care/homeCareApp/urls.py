from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('nuevoSignoVital', views.nuevoSignoVital, name='nuevoSignoVital'),
    path('getSignoVital/<int:id>', views.getSignoVital, name='getSignoVital'),
    
    path('nuevoRol', views.nuevoRol, name='nuevoRol'),
    path('getRol/<int:id>', views.getRol, name='getRol'),

    path('getUsuario/<int:id>', views.getUsuario, name='getUsuario'),

    path('nuevoPersona', views.nuevoPersona, name='nuevoPersona'),
    path('getPersona/<int:id>', views.getPersona, name='getPersona'),
    path('getPeople', views.getPeople, name='getPeople'),

    path('nuevoPaciente', views.nuevoPaciente, name='nuevoPaciente'),
    path('getPaciente/<int:id>', views.getPaciente, name='getPaciente'),
    path('getAllPatients', views.getAllPatients, name='getAllPatients'),

    path('nuevoMedico', views.nuevoMedico, name='nuevoMedico'),
    path('getMedico/<int:id>', views.getMedico, name='getMedico'),

    path('nuevoEspecialidad', views.nuevoEspecialidad, name='nuevoEspecialidad'),
    path('getEspecialidad/<int:id>', views.getEspecialidad, name='getEspecialidad'),
    path('getEspecialidades', views.getEspecialidades, name='getEspecialidades'),

    path('nuevoFamiliar', views.nuevoFamiliar, name='nuevoFamiliar'),
    path('getFamiliar/<int:id>', views.getFamiliar, name='getFamiliar'),

    path('nuevoRegistro_SV', views.nuevoRegistro_SV, name = 'nuevoRegistro_SV'),
    path('getRegistro_SV/<int:id>', views.getRegistro_SV, name = 'getRegistro_SV'),
    
    path('nuevoDiagnostico', views.nuevoDiagnostico, name='nuevoDiagnostico'),
    path('getDiagnostico/<int:id>', views.getDiagnostico, name='getDiagnostico'),
    path('getAllDiagnostico', views.getAllDiagnostico, name= 'getAllDiagnostico'),

    path('nuevaSugerencia', views.nuevaSugerencia, name='nuevaSugerencia'),
    path('getSugerencia/<int:id>', views.getSugerencia, name='getSugerencia'),
    path('getAllSugerencias', views.getAllSugerencias, name= 'getAllSugerencias'),

]
