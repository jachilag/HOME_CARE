from django.db import models
from django.utils import timezone

class Signos_vitales(models.Model):
    ID_SIGNO_VITAL = models.AutoField(primary_key=True)
    Tipo_Signo = models.CharField(max_length=60)
    
    def __str__(self):
        return self.Tipo_Signo

class Rol(models.Model):
    ID_ROL = models.AutoField(primary_key=True)
    Rol = models.CharField(max_length=60)

class Usuarios(models.Model):
    ID_LOGIN= models.BigIntegerField(primary_key=True) #corregir este campo ya que no es autoincremental y si es varchar
    ID_ROL  = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Password = models.CharField(max_length=60) 

class Persona(models.Model):
    ID_PERSONA = models.AutoField(primary_key=True)
    Identificacion = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=60)
    Apellido = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=60)
    Genero = models.CharField(max_length=60)#corregir campo para que sea foraneo de una nueva tabla genero
    Email = models.CharField(max_length=60)

class Auxiliar(models.Model):
    ID_AUXILIAR = models.AutoField(primary_key=True)
    ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Enfermero(models.Model):
    ID_ENFERMERO = models.AutoField(primary_key=True)
    ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Familiar(models.Model):
    ID_FAMILIAR = models.AutoField(primary_key=True)
    ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=60)

class Especialidad (models.Model):
    ID_ESPECIALIDAD = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=60)

class Medico(models.Model):
    ID_MEDICO = models.AutoField(primary_key=True)
    ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)
    ID_ESPECIALIDAD = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null= True)
    Registro = models.CharField(max_length=60)

class Paciente(models.Model):
    ID_PACIENTE = models.AutoField(primary_key=True)
    Persona_ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Medico_ID_MEDICO = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    Familiar_ID_FAMILIAR = models.ForeignKey(Familiar, on_delete=models.CASCADE, null=True)
    Direccion = models.CharField(max_length=255)
    Ciudad = models.CharField(max_length=60)
    Latitud = models.DecimalField(max_digits= 11, decimal_places= 8)
    Longitud = models.DecimalField(max_digits= 11, decimal_places= 8)
    Fecha_Nacimiento = models.DateField()

class Registro_SV(models.Model):
    ID_REGISTRO_SV = models.AutoField(primary_key=True)
    SV_ID_SIGNO_VITAL = models.ForeignKey(Signos_vitales, on_delete = models.CASCADE)
    Paciente_ID_PACIENTE = models.ForeignKey(Paciente, on_delete = models.CASCADE)
    Medida = models.DecimalField(max_digits = 6, decimal_places = 3)
    Fecha_Hora = models.DateTimeField(default = timezone.now, blank = False)



class T_Diagnostico(models.Model):
    ID_DIAGNOSTICO = models.BigAutoField(primary_key=True)
    ID_PACIENTE = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ID_MEDICO = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Diagnostico = models.TextField()
    fecha_hora = models.DateTimeField()

class T_Sugerencias(models.Model):
    ID_SUGERENCIAS = models.AutoField(primary_key=True)
    ID_MEDICO = models.ForeignKey(Medico, on_delete=models.CASCADE)
    ID_DIAGNOSTICO = models.ForeignKey(T_Diagnostico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    descripcion = models.TextField()
