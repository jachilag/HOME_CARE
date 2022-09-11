
import datetime
import email
import json
import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from .models import Signos_vitales, Rol, Usuarios, Persona, Auxiliar, Enfermero, Familiar, Especialidad, Medico, Paciente, Registro_SV, T_Diagnostico, T_Sugerencias


def home(request):
    return HttpResponse("Bienvenido a su aplicacion HOME CARE")

def nuevoSignoVital(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #seccion para validacion de existencia de registros en tablas foraneas

            #instancia de la clase
            signoVital = Signos_vitales(
                Tipo_Signo = data["signo_vital"]
            )
            signoVital.save()
            return HttpResponse("Signo Vital agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getSignoVital(request, id):
    if request.method == 'GET':
        try:
            signoVital = Signos_vitales.objects.filter(ID_SIGNO_VITAL = id).first()
            if(not signoVital):
                return HttpResponseBadRequest("No existe Signo Vital")

            data = {
                "ID_SIGNO_VITAL": signoVital.ID_SIGNO_VITAL,
                "Tipo_Signo": signoVital.Tipo_Signo
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoRol(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #seccion para validacion de existencia de registros en tablas foraneas

            #instancia de la clase
            rol = Rol(
                Rol = data["Rol"]
            )
            rol.save()


            return HttpResponse("nuevo Rol agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getRol(request, id):
    if request.method == 'GET':
        try:

            rol = Rol.objects.filter(ID_ROL = id).first()
            if(not rol):
                return HttpResponseBadRequest("No existe Rol")
            data = {
                "ID_ROL": rol.ID_ROL,
                "Rol": rol.Rol
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getUsuario(request, id):
    if request.method == 'GET':
        try:
            usuario = Usuarios.objects.filter(ID_LOGIN = id).first()
            if(not usuario):
                return HttpResponseBadRequest("No existe Usuario")

            data = {
                "ID_LOGIN" : usuario.ID_LOGIN,
                "ROL" : usuario.ID_ROL.Rol,
                "Password" : usuario.Password
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas
            rol = Rol.objects.filter(ID_ROL = data["ID_ROL"]).first()
            if(not rol):
                return HttpResponseBadRequest("No existe Rol")
            
            #evaluar si hay solo letras en nombres y apellidos
            if (re.search('[0-9]',data["Nombre"])):
                return HttpResponseBadRequest("Nombre incorrecto")

            if (re.search('[0-9]',data["Apellido"])):
                return HttpResponseBadRequest("Apellido incorrecto")

            #evaluar si hay numeros en el telefono
            if (re.search('[a-zA-Z]',data["Telefono"])):
                return HttpResponseBadRequest("Telefono incorrecto")

            #evaluar si correo electronico tiene el @
            if (not re.search('@',data["Email"])):
                return HttpResponseBadRequest("correo electronico incorrecto")
            
            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = rol,
                Password = data["Password"]
            )

            persona = Persona(
                Identificacion = usuario,
                Nombre = data["Nombre"],
                Apellido = data["Apellido"],
                Telefono = data["Telefono"],
                Genero = data["Genero"],
                Email = data["Email"]
            )

            usuario.save()
            persona.save()
            return HttpResponse("Persona agregada")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getPersona(request, id):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(ID_PERSONA = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe Persona")

            data = {
                "ID_PERSONA":persona.ID_PERSONA,
                "Identificacion":persona.Identificacion.ID_LOGIN,
                "Nombre":persona.Nombre,
                "Apellido":persona.Apellido,
                "Telefono":persona.Telefono,
                "Genero":persona.Genero,
                "Email":persona.Email,
                "Rol" : persona.Identificacion.ID_ROL.Rol
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getPeople(request):
    if request.method == 'GET':
        try:
            personas = Persona.objects.all()
            if (not personas):
                return HttpResponseBadRequest("No existen personas cargados.")
            
            allPeople = []
            for per in personas:
                data = {
                    "Identificacion" : per.Identificacion.ID_LOGIN,
                    "Rol" : per.Identificacion.ID_ROL.Rol,
                    "Nombre" : per.Nombre,
                    "Apellido" : per.Apellido,
                    "Telefono" : per.Telefono,
                }
                allPeople.append(data)

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(allPeople)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas
            persona = Persona.objects.filter(Identificacion = data["Identificacion"]).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 3):
                return HttpResponseBadRequest("este Usuario no esta asociado como paciente")
            
            pac = Paciente.objects.filter(Persona_ID_PERSONA = persona.ID_PERSONA).first()
            if(pac):
                return HttpResponseBadRequest("Ya esta registrado como paciente")

            #instancia de la clase
            paciente = Paciente(
                Persona_ID_PERSONA = persona,
                Medico_ID_MEDICO = data["Medico_ID_MEDICO"],
                Familiar_ID_FAMILIAR = data["Familiar_ID_FAMILIAR"],
                Direccion = data["Direccion"],
                Ciudad = data["Ciudad"],
                Latitud = data["Latitud"],
                Longitud = data["Longitud"],
                Fecha_Nacimiento = data["Fecha_Nacimiento"]
            )
            
            paciente.save()
            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

#obtenemos paciente por su documento
def getPaciente(request, id):
    if request.method == 'GET':
        try:
            
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 3):
                return HttpResponseBadRequest("Este Usuario no es paciente")

            paciente = Paciente.objects.filter(Persona_ID_PERSONA = persona.ID_PERSONA).first()

            print(paciente.Medico_ID_MEDICO)
            data = {
                "Identificacion" : id,
                "Medico_ID_MEDICO" : paciente.Medico_ID_MEDICO.ID_MEDICO if paciente.Medico_ID_MEDICO != None else None,
                "Familiar_ID_FAMILIAR" : paciente.Familiar_ID_FAMILIAR.ID_FAMILIAR if paciente.Familiar_ID_FAMILIAR != None else None,
                "Nombre" : persona.Nombre,
                "Apellido" : persona.Apellido,
                "Genero" : persona.Genero,
                "Telefono" : persona.Telefono,
                "Fecha_Nacimiento" : str(paciente.Fecha_Nacimiento),
                "Direccion" : paciente.Direccion,
                "Ciudad" : paciente.Ciudad,
                "Latitud" : float(paciente.Latitud),
                "Longitud" : float(paciente.Longitud)
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getAllPatients(request):
    if request.method == 'GET':
        try:
            pacientes = Paciente.objects.all()
            if (not pacientes):
                return HttpResponseBadRequest("No existen Pacientes cargados.")
            
            allPatients = []
            for pat in pacientes:
                data = {
                    "Identificacion" : pat.Persona_ID_PERSONA.Identificacion.ID_LOGIN,
                    "Nombre" : pat.Persona_ID_PERSONA.Nombre,
                    "Apellido" : pat.Persona_ID_PERSONA.Apellido,
                    "Telefono" : pat.Persona_ID_PERSONA.Telefono,
                    "Direccion" : pat.Direccion,
                }
                allPatients.append(data)

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(allPatients)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoEspecialidad(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas

            #instancia de la clase


            #especialidad.save()
            return HttpResponse("Signo Vital agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getEspecialidad(request, id):
    if request.method == 'GET':
        try:


            data = {

            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas

            #instancia de la clase


            #medico.save()
            return HttpResponse("Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getMedico(request, id):
    if request.method == 'GET':
        try:
            usuario = Usuarios.objects.filter(ID_LOGIN = id).first()
            if(not usuario):
                return HttpResponseBadRequest("No existe Usuario")

            data = {

            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas

            #instancia de la clase


            #familiar.save()
            return HttpResponse("Familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getFamiliar(request, id):
    if request.method == 'GET':
        try:
            usuario = Usuarios.objects.filter(ID_LOGIN = id).first()
            if(not usuario):
                return HttpResponseBadRequest("No existe Usuario")

            data = {

            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

