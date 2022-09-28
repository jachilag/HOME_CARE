from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('nuevoSignoVital', views.nuevoSignoVital, name='nuevoSignoVital'),
    path('getSignoVital/<int:id>', views.getSignoVital, name='getSignoVital'),
    
    path('nuevoRol', views.nuevoRol, name='nuevoRol'),
    path('getRol/<int:id>', views.getRol, name='getRol'),
    path('updateRol', views.updateRol, name='updateRol'),
    path('deleteRol/<int:id>', views.deleteRol, name='deleteRol'),

    path('login', views.login, name='login'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'), 

    path('getPersona/<int:id>', views.getPersona, name='getPersona'),
    path('getPersonas', views.getPersonas, name='getPersonas'),
    path('deletePersona/<int:id>', views.deletePersona, name='deletePersona'), 

    path('nuevoPaciente', views.nuevoPaciente, name='nuevoPaciente'),
    path('getPaciente/<int:id>', views.getPaciente, name='getPaciente'),
    path('getPacientes', views.getPacientes, name='getPacientes'),
    path('deletePaciente/<int:id>', views.deletePaciente, name='deletePaciente'), 
    path('updatePaciente/<int:id>', views.updatePaciente, name='updatePaciente'),
    path('updatePaciente_Medico/<int:id>', views.updatePaciente_Medico, name='updatePaciente_Medico'),
    path('updatePaciente_Familiar/<int:id>', views.updatePaciente_Familiar, name='updatePaciente_Familiar'),

    path('nuevoMedico', views.nuevoMedico, name='nuevoMedico'),
    path('getMedico/<int:id>', views.getMedico, name='getMedico'),
    path('deleteMedico/<int:id>', views.deleteMedico, name='deleteMedico'), 
    path('updateMedico/<int:id>', views.updateMedico, name='updateMedico'), 
    path('getMisPacientes/<int:id>', views.getMisPacientes, name='getMisPacientes'), 

    path('nuevoEspecialidad', views.nuevoEspecialidad, name='nuevoEspecialidad'),
    path('getEspecialidad/<int:id>', views.getEspecialidad, name='getEspecialidad'),
    path('getEspecialidades', views.getEspecialidades, name='getEspecialidades'),
    path('deleteEspecialidad/<int:id>', views.deleteEspecialidad, name='deleteEspecialidad'), 

    path('nuevoFamiliar', views.nuevoFamiliar, name='nuevoFamiliar'),
    path('getFamiliar/<int:id>', views.getFamiliar, name='getFamiliar'),
    path('deleteFamiliar/<int:id>', views.deleteFamiliar, name='deleteFamiliar'), 
    path('updateFamiliar/<int:id>', views.updateFamiliar, name='updateFamiliar'),

    path('nuevoAuxiliar', views.nuevoAuxiliar, name='nuevoAuxiliar'),
    path('getAuxiliar/<int:id>', views.getAuxiliar, name='getAuxiliar'),
    path('deleteAuxiliar/<int:id>', views.deleteAuxiliar, name='deleteAuxiliar'), 

    path('nuevoEnfermero', views.nuevoEnfermero, name='nuevoEnfermero'),
    path('getEnfermero/<int:id>', views.getEnfermero, name='getEnfermero'),
    path('deleteEnfermero/<int:id>', views.deleteEnfermero, name='deleteEnfermero'), 

    path('nuevoRegistro_SV', views.nuevoRegistro_SV, name = 'nuevoRegistro_SV'),
    path('getRegistro_SV/<int:id>', views.getRegistro_SV, name = 'getRegistro_SV'),
    
    path('nuevoDiagnostico', views.nuevoDiagnostico, name='nuevoDiagnostico'),
    path('getDiagnostico/<int:id>', views.getDiagnostico, name='getDiagnostico'),
    path('getDiagnosticos', views.getDiagnosticos, name= 'getDiagnosticos'),

    path('nuevaSugerencia', views.nuevaSugerencia, name='nuevaSugerencia'),
    path('getSugerencia/<int:id>', views.getSugerencia, name='getSugerencia'),
    path('getSugerencias', views.getSugerencias, name= 'getSugerencias'),

]
