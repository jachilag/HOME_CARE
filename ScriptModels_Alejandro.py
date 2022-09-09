from django.db import models

# Create your models here.

class Signos_vitales(models.Model):
    ID_SIGNO_VITAL = models.AutoField(primary_key=True)
    Tipo_Signo = models.CharField(max_length=60)

class Paciente(models.Model):
    ID_PACIENTE = models.AutoField(primary_key=True)
    Persona_ID_PERSONA = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Medico_ID_MEDICO = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Familiar_ID_FAMILIAR = models.ForeignKey(Familiar, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=255)
    Ciudad = models.CharField(max_length=60)
    Latitud = models.DecimalField(max_digits= 11, decimal_places= 8)
    Longitud = models.DecimalField(max_digits= 11, decimal_places= 8)
    Fecha_Nacimiento = models.DateField()
    


class Registro_SV(models.Model):
    ID_REGISTRO_SV = models.AutoField(primary_key=True)
    SV_ID_SIGNO_VITAL = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Paciente_ID_PACIENTE = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Medida = models.DecimalField(max_digits= 6, decimal_places= 3)
    Fecha_Hora = models.TimeField()
    Fecha_Nacimiento = models.CharField(max_length=128)
    

