import json
import datetime
import mimetypes
import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError
from django.forms.models import model_to_dict
from django.core import serializers

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

def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            rol = data['ID_ROL']
            identificacion = data['Identificacion']
            password = data['password']

            usuario = Usuarios.objects.filter(ID_LOGIN = identificacion, password = password, Rol = rol).first()
            if(not usuario):
                return HttpResponse("No existe Usuario", status = 401)

            data = {
                "ID_LOGIN" : usuario.ID_LOGIN,
                "ROL" : usuario.ID_ROL.Rol,
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseBadRequest("Error de servidor")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

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
            if(verificarInfoNuevo(data) != "verificado"):
                return HttpResponseBadRequest(verificarInfoNuevo(data))

            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = 3,
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

            usuario.save()
            persona.save()
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
            esp = Especialidad.objects.filter(especialidad = data["especialidad"]).first()
            
            if(esp != None):
                return HttpResponseBadRequest("Ya existe la especialidad") 

            #instancia de la clase
            especialidad = Especialidad(
                especialidad = data["especialidad"]
            )
            especialidad.save()
            return HttpResponse("Especialidad agregada")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getEspecialidad(request, id):
    if request.method == 'GET':
        try:
            especialidad = Especialidad.objects.filter(ID_ESPECIALIDAD = id).first()
            print(especialidad)

            if(especialidad == None):
                return HttpResponseBadRequest("No existe la especialidad")

            data = {
                "especialidad" : especialidad.especialidad
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getEspecialidades(request):
    if request.method == 'GET':
        try:
            especialidades = Especialidad.objects.all()
            print(especialidades)
            if (not especialidades):
                return HttpResponseBadRequest("No existen especialidades cargadas.")
            
            allEspecialidades = []
            for esp in especialidades:
                data = {
                    "id" : esp.ID_ESPECIALIDAD,
                    "Especialidad" : esp.especialidad,
                }
                allEspecialidades.append(data)

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(allEspecialidades)
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
            if(verificarInfoNuevo(data) != "verificado"):
                return HttpResponseBadRequest(verificarInfoNuevo(data))

            #seccion para validacion de existencia de especialidad valida
            especialidad = Especialidad.objects.filter(ID_ESPECIALIDAD = data["Id_especialidad"]).first()
            if(not especialidad):
                return HttpResponseBadRequest("No existe la especialidad indicada")

            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = 1,
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

            medico = Medico(
                ID_PERSONA = persona,
                ID_ESPECIALIDAD = especialidad,
                Registro = data["Registro"]
            )

            usuario.save()
            persona.save()
            medico.save()
            return HttpResponse("Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getMedico(request, id):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("este Usuario no esta asociado como Medico")

            medico = Medico.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()

            data = {
                "Identificacion" : id,
                "Nombre" : persona.Nombre,
                "Apellido" : persona.Apellido,
                "Genero" : persona.Genero,
                "Telefono" : persona.Telefono,
                "Email" : persona.Email,
                "ID_ESPECIALIDAD" : medico.ID_ESPECIALIDAD.especialidad,
                "Registro" : medico.Registro,
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
            if(verificarInfoNuevo(data) != "verificado"):
                return HttpResponseBadRequest(verificarInfoNuevo(data))

            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = 4,
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

            familiar = Familiar(
                ID_PERSONA = persona,
                parentesco = data["parentesco"]
            )

            usuario.save()
            persona.save()
            familiar.save()
            return HttpResponse("Familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getFamiliar(request, id):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 4):
                return HttpResponseBadRequest("este Usuario no esta asociado como familiar")

            familiar = Familiar.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()

            data = {
                "Identificacion" : id,
                "Nombre" : persona.Nombre,
                "Apellido" : persona.Apellido,
                "Genero" : persona.Genero,
                "Telefono" : persona.Telefono,
                "Email" : persona.Email,
                "Parentesco" : familiar.parentesco,
            }
            
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoAuxiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas
            if(verificarInfoNuevo(data) != "verificado"):
                return HttpResponseBadRequest(verificarInfoNuevo(data))

            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = 2,
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

            auxiliar = Auxiliar(
                ID_PERSONA = persona,
            )

            usuario.save()
            persona.save()
            auxiliar.save()
            return HttpResponse("Auxiliar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAuxiliar(request, id):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 2):
                return HttpResponseBadRequest("este Usuario no esta asociado como auxiliar")

            auxiliar = Auxiliar.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()

            data = {
                "Identificacion" : id,
                "Nombre" : persona.Nombre,
                "Apellido" : persona.Apellido,
                "Genero" : persona.Genero,
                "Telefono" : persona.Telefono,
                "Email" : persona.Email,
            }
            
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoEnfermero(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            #seccion para validacion de existencia de registros en tablas foraneas
            if(verificarInfoNuevo(data) != "verificado"):
                return HttpResponseBadRequest(verificarInfoNuevo(data))

            #instancia de la clase
            usuario = Usuarios(
                ID_LOGIN = data["Identificacion"],
                ID_ROL = 5,
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

            enfermero = Enfermero(
                ID_PERSONA = persona,
            )

            usuario.save()
            persona.save()
            enfermero.save()
            return HttpResponse("enfermero agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getEnfermero(request, id):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 5):
                return HttpResponseBadRequest("este Usuario no esta asociado como enfermero")

            enfermero = Enfermero.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()

            data = {
                "Identificacion" : id,
                "Nombre" : persona.Nombre,
                "Apellido" : persona.Apellido,
                "Genero" : persona.Genero,
                "Telefono" : persona.Telefono,
                "Email" : persona.Email,
            }
            
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoRegistro_SV (request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #data_valitation Paciente model
            paciente = Paciente.objects.filter(ID_PACIENTE = data["Paciente_ID_PACIENTE"]).first()
            if(not paciente):
                return HttpResponseBadRequest ("El paciente indicado no se encuentra registrado")

            signo_vital = Signos_vitales.objects.filter(ID_SIGNO_VITAL = data["SV_ID_SIGNO_VITAL"]).first()   
            if (not signo_vital):
                return HttpResponseBadRequest ("El tipo de medida no existe")

            #New Registro_SV object
            registro_sv = Registro_SV(
                SV_ID_SIGNO_VITAL = signo_vital,
                Paciente_ID_PACIENTE = paciente,
                Medida = data["Medida"],
                Fecha_Hora = datetime.datetime.now()
                )     

            registro_sv.save()
            return HttpResponse("Se registro el dato exitosamente")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getRegistro_SV(request, id):
    if request.method == 'GET':
        try:
            #data_valitation Registro_SV model
            registro_sv = Registro_SV.objects.filter(ID_REGISTRO_SV = id).first()
            if(not registro_sv):
                return HttpResponseBadRequest ("No se encontro registro")
                
            data ={
                "Signo_vital" : registro_sv.SV_ID_SIGNO_VITAL.Tipo_Signo,
                "Identificacion" : registro_sv.Paciente_ID_PACIENTE.Persona_ID_PERSONA.Identificacion.ID_LOGIN,
                "Medida" : float(registro_sv.Medida),
                "Fecha_Hora": str(registro_sv.Fecha_Hora),
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoDiagnostico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            paciente = Paciente.objects.filter(Persona_ID_PERSONA = data["ID_PACIENTE"]).first()
            if(not paciente):
                return HttpResponseBadRequest("El paciente indicado no se encuentra registrado")
            
            if(paciente.Persona_ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 3):
                return HttpResponseBadRequest("Este usuario no está registrado como paciente")
            
            med = Medico.objects.filter(ID_PERSONA = data["ID_MEDICO"]).first()
            if(not med):
                return HttpResponseBadRequest("El médico indicado no se encuentra registado")
            
            if(med.ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("Este usuario no está registrado como médico")

            diagnostico = T_Diagnostico(
                ID_PACIENTE = paciente,
                ID_MEDICO = med,
                Diagnostico = data["Diagnostico"], 
                fecha_hora = datetime.datetime.now()          
            )

            diagnostico.save()
            return HttpResponse("Diagostico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos procesados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método invalido")
        
def getDiagnostico(request, id):
    if request.method == 'GET':
        try: 
            
            diag = T_Diagnostico.objects.filter(ID_DIAGNOSTICO = id).first()
            #persona = Persona.objects.filter()
            #paciente = Paciente.objects.filter(Persona_ID_PERSONA = persona.ID_PERSONA).first()

            if(not diag):
                return HttpResponseBadRequest("No existe un diagnóstico con esa numeración")
            
            data = {
                "Id_Diagnostico": id,
                "Id_Paciente": diag.ID_PACIENTE.Persona_ID_PERSONA.Identificacion.ID_LOGIN,
                "Nombre_Medico": diag.ID_MEDICO.ID_PERSONA.Nombre,
                "Diagnostico": str(diag.Diagnostico),
                "Fecha_hora": str(diag.fecha_hora)
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getAllDiagnosticos(request, id_paciente):
    if request.method == 'GET':
        try:
            diagnosticos = T_Diagnostico.objects.filter(ID_PACIENTE = id_paciente)
            if(not diagnosticos):
                return HttpResponseBadRequest("No existen diagnósticos")

            allDiagnosticos = []
            for diag in diagnosticos:
                data = {
                   "Id_Diagnostico": diag.ID_DIAGNOSTICO,
                   "Id_Paciente": id_paciente,
                   "Nombre_Medico": diag.ID_MEDICO.ID_PERSONA.Nombre,
                   "Diagnostico": str(diag.Diagnostico),
                   "Fecha_hora": str(diag.fecha_hora)
                }
                allDiagnosticos.append(data)

            return HttpResponse(allDiagnosticos, content_type = "text/json")
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevaSugerencia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            diagnostico = T_Diagnostico.objects.filter(ID_DIAGNOSTICO = data["ID_DIAGNOSTICO"]).first()
            if(not diagnostico):
                return HttpResponseBadRequest("No existe ningún diagnostico con esa numeración para hacerle una sugerencia")
            
            med = Medico.objects.filter(ID_PERSONA = data["ID_MEDICO"]).first()
            if(not med):
                return HttpResponseBadRequest("El médico indicado no se encuentra registado")
            
            if(med.ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("Este usuario no está registrado como médico")   
            
            sugerencia = T_Sugerencias(
                ID_DIAGNOSTICO = diagnostico,
                ID_MEDICO = med,
                descripcion = data["descripcion"]                
            )

            sugerencia.save()
            return HttpResponse("Sugerencia agregada")
        except:
            return HttpResponseBadRequest("Error en los datos procesados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método invalido")

def getSugerencia(request, id):
    if request.method == 'GET':
        try: 
            sugerencia = T_Sugerencias.objects.filter(ID_SUGERENCIAS = id).first()
            if(not sugerencia):
                return HttpResponseBadRequest("No existe una sugerencia con esa numeración")
            
            data = {
                "Id_Sugerencia": id,
                "Nombre_Medico": sugerencia.ID_MEDICO.ID_PERSONA.Nombre,
                "Sugerencia": str(sugerencia.descripcion),
                "Fecha_hora": str(sugerencia.fecha_hora)
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getAllSugerencias(request, id_diagnostico):
    if request.method == 'GET':
        try:
            sugerencias = T_Sugerencias.objects.filter(ID_DIAGNOSTICO = id_diagnostico)
            if(not sugerencias):
                return HttpResponseBadRequest("No existen sugerencias")
            
            allSugerencias = []
            for sug in sugerencias:
                data = {
                   "Id_Sugerencia": sug.ID_SUGERENCIAS,
                   "Id_Diagnostico": sug.ID_DIAGNOSTICO.ID_DIAGNOSTICO,
                   "Id_Paciente" : sug.ID_DIAGNOSTICO.ID_PACIENTE.Persona_ID_PERSONA.Identificacion,
                   "Nombre_Medico": sug.ID_MEDICO.ID_PERSONA.Nombre,
                   "Sugerencia": str(sug.descripcion),
                   "Fecha_hora": str(sug.fecha_hora)
                }
                allSugerencias.append(data)

            return HttpResponse(allSugerencias, content_type = "text/json")
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")



def verificarInfoNuevo(data):
    
    #evaluar si hay solo letras en nombres y apellidos
    if (re.search('[0-9]',data["Nombre"])):
        return "Nombre incorrecto"

    if (re.search('[0-9]',data["Apellido"])):
        return "Apellido incorrecto"

    #evaluar si hay numeros en el telefono
    if (re.search('[a-zA-Z]',data["Telefono"])):
        return "Telefono incorrecto"

    #evaluar si correo electronico tiene el @
    if (not re.search('@',data["Email"])):
        return "correo electronico incorrecto"
    
    persona = Persona.objects.filter(Identificacion = data["Identificacion"]).first()
    if(persona):
        return "Ya existe un usuario con ese documento"
    
    return "verificado"
