from django.contrib import admin
from .models import Signos_vitales, Rol, Usuarios, Persona, Auxiliar, Enfermero, Familiar, Especialidad, Medico, Paciente, Registro_SV, T_Diagnostico, T_Sugerencias
admin.site.register([Signos_vitales, Rol, Usuarios, Persona, Auxiliar, Enfermero, Familiar, Especialidad, Medico, Paciente, Registro_SV, T_Diagnostico, T_Sugerencias])