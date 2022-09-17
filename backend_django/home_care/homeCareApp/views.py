import json
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
            
            #seccion para validacion de existencia de persona en DB
            persona = Persona.objects.filter(Identificacion = data["Id_persona"]).first()
            if(not persona):
                return HttpResponseBadRequest("No existe ninguna persona con esa identificación")

            #seccion para validacion de existencia de persona en DB
            especialidad = Especialidad.objects.filter(ID_ESPECIALIDAD = data["Id_especialidad"]).first()
            if(not especialidad):
                return HttpResponseBadRequest("No existe ninguna la especialidad indicada")

            if(persona.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("No esta identificado como médico este usuario")

            med = Medico.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()
            if(med):
                return HttpResponseBadRequest("Ya esta registrado como Medico")

            # instancia de la clase
            # persona.medico_set.create(Registro=data["Registro"],
            #             ID_ESPECIALIDAD=data["Id_especialidad"])
            medico = Medico(
                ID_PERSONA = persona,
                ID_ESPECIALIDAD = especialidad,
                Registro = data["Registro"]
            )
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
                "ID_MEDICO" : id,
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

            #seccion para validacion de existencia de persona en DB
            persona = Persona.objects.filter(Identificacion = data["ID_PERSONA"]).first()
            if(not persona):
                return HttpResponseBadRequest("No existe ninguna persona con esa identificación")

            if(persona.Identificacion.ID_ROL.ID_ROL != 4):
                return HttpResponseBadRequest("No esta identificado como Familiar este usuario")

            fam = Familiar.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()
            if(fam):
                return HttpResponseBadRequest("Ya esta registrado como Familiar")

            #instancia de la clase
            familiar = Familiar(
                ID_PERSONA = persona,
                parentesco = data["parentesco"]
            )

            familiar.save()
            return HttpResponse("Familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getFamiliar(request, id):
    if request.method == 'GET':
        try:
            #seccion para validacion de existencia de persona en DB
            persona = Persona.objects.filter(Identificacion = id).first()
            if(not persona):
                return HttpResponseBadRequest("No existe un usuario con ese documento")

            if(persona.Identificacion.ID_ROL.ID_ROL != 4):
                return HttpResponseBadRequest("este Usuario no esta asociado como Familiar")

            familiar = Familiar.objects.filter(ID_PERSONA = persona.ID_PERSONA).first()

            data = {
                "ID_FAMILIAR" : id,
                "parentesco" : familiar.parentesco
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
            request_data = json.loads(request.body)
            #data_valitation Paciente model
            paciente = Paciente.objects.filter(ID_PACIENTE = request_data["Paciente_ID_PACIENTE"]).first()
            if(not paciente):
                return HttpResponseBadRequest ("El paciente indicado no se encuentra registrado")
            signo_vital = Signos_vitales.objects.filter(ID_SIGNO_VITAL = request_data["SV_ID_SIGNO_VITAL"]).first()   
            if (not signo_vital):
                return HttpResponseBadRequest ("El tipo de medida no existe")
            #New Registro_SV object
            registro_sv = Registro_SV(
                SV_ID_SIGNO_VITAL = signo_vital,
                Paciente_ID_PACIENTE = paciente,
                Medida = request_data["Medida"]
                #Fecha_Hora = timezone.now()
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
            registro_sv_query = serializers.serialize('json', [registro_sv,])
            return HttpResponse(registro_sv_query, content_type = "text/json") 

            #Metodo Fallido No es posible serializar modelos o funciones de django como DateTime o Decimal.
            #registro_sv_query = {
                #"ID_REGISTRO_SV" : id,
                #"SV_ID_SIGNO_VITAL" : registro_sv.SV_ID_SIGNO_VITAL.Tipo_Signo,
                #"Paciente_ID_PACIENTE" : registro_sv.Paciente_ID_PACIENTE.ID_PACIENTE,
                #"Medida" : registro_sv.Medida,
                #"Fecha_Hora" : registro_sv.Fecha_Hora,
            #}
            #data = json.dumps(registro_sv_query)
            #return HttpResponse(data, content_type = "text/json")

            #registro_sv_query = model_to_dict(registro_sv)

        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoDiagnostico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            paciente = Paciente.objects.filter(Persona_ID_PERSONA__Identificacion = data["ID_PACIENTE"]).first()
            if(not paciente):
                return HttpResponseBadRequest("El paciente indicado no se encuentra registrado")
            

            if(paciente.Persona_ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 3):
                return HttpResponseBadRequest("Este usuario no está registrado como paciente")
            
            med = Medico.objects.filter(ID_PERSONA__Identificacion = data["ID_MEDICO"]).first()
            if(not med):
                return HttpResponseBadRequest("El médico indicado no se encuentra registado")
            
            if(med.ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("Este usuario no está registrado como médico")

            #return HttpResponse("Debug")

            diagnostico = T_Diagnostico(
                ID_PACIENTE = paciente,
                ID_MEDICO = med,
                Diagnostico = data["Diagnostico"]                
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
                "Id_Medico": diag.ID_MEDICO.ID_PERSONA.Nombre,
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

def getAllDiagnostico(request):
    if request.method == 'GET':
        try:
            diagnosticos = T_Diagnostico.objects.all()
            if(not diagnosticos):
                return HttpResponseBadRequest("No existen diagnósticos")

            allDiagnosticos = []
            for diag in diagnosticos:
                #data = serializers.serialize('json', [diag,])

                data = {
                   "Id_Diagnostico": diag.ID_DIAGNOSTICO,
                   "Id_Paciente": diag.ID_PACIENTE.Persona_ID_PERSONA.Identificacion.ID_LOGIN,
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
            
            med = Medico.objects.filter(ID_PERSONA__Identificacion = data["ID_MEDICO"]).first()
            if(not med):
                return HttpResponseBadRequest("El médico indicado no se encuentra registado")
            
            if(med.ID_PERSONA.Identificacion.ID_ROL.ID_ROL != 1):
                return HttpResponseBadRequest("Este usuario no está registrado como médico")   
            
            #return HttpResponse("Debug")

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
            
            sug = T_Sugerencias.objects.filter(ID_SUGERENCIAS = id).first()
            #persona = Persona.objects.filter()
            #paciente = Paciente.objects.filter(Persona_ID_PERSONA = persona.ID_PERSONA).first()

            if(not sug):
                return HttpResponseBadRequest("No existe una sugerencia con esa numeración")
            
            data = {
                "Id_Sugerencia": id,
                "Id_Medico": sug.ID_MEDICO.ID_PERSONA.Nombre,
                "Sugerencia": str(sug.descripcion),
                "Fecha_hora": str(sug.fecha_hora)
            }

            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getAllSugerencias(request):
    if request.method == 'GET':
        try:
            sugerencias = T_Sugerencias.objects.all()
            if(not sugerencias):
                return HttpResponseBadRequest("No existen sugerencias")
            
            allSugerencias = []
            for sug in sugerencias:
                #data = serializers.serialize('json', [diag,])

                data = {
                   "Id_Sugerencia": sug.ID_SUGERENCIAS,
                   "Id_Diagnostico": sug.ID_DIAGNOSTICO.ID_DIAGNOSTICO,
                   "Nombre_Medico": sug.ID_MEDICO.ID_PERSONA.Nombre,
                   "Sugerencia": str(sug.descripcion),
                   "Fecha_hora": str(sug.fecha_hora)
                }
                allSugerencias.append(data)
            #return HttpResponse(allSugerencias)

            return HttpResponse(allSugerencias, content_type = "text/json")
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
