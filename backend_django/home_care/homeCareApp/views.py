import email
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from .models import Signos_vitales, Rol, Usuarios, Persona, Auxiliar, Enfermero, Familiar, Especialidad, Medico, Paciente, Registro_SV, T_Diagnostico, T_Sugerencias

def home(request):
    return HttpResponse("Bienvenido a su aplicacion HOME CARE")

def nuevoUsuario(request):
    if request.method == 'POST':
        try:

            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoPersona(request):
    if request.method == 'POST':
        try:

            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoPaciente(request):
    if request.method == 'POST':
        try:

            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoMedico(request):
    if request.method == 'POST':
        try:

            return HttpResponse("Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoFamiliar(request):
    if request.method == 'POST':
        try:

            return HttpResponse("Familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllPacientes(request):
    if request.method == 'GET':
        try:

            return None
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOnePaciente(request, id):
    if request.method == 'GET':
        try:

            return None
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

