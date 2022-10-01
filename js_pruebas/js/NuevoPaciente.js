
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const newEntUrl = host + 'nuevoPaciente';
const getUsuUrl = host + 'getPersonas';
let usuarios = [];

function create() {
    getUsuarios()
    setTimeout(function(){
        var identificacion = document.getElementById("Identificacion").value.trim();
        var Password = document.getElementById("Password").value.trim();
        var Nombre = document.getElementById("Nombre").value.trim();
        var Apellido = document.getElementById("Apellido").value.trim();
        var Telefono = document.getElementById("Telefono").value.trim();
        var Genero = document.getElementById("Genero").value.trim();
        var Email = document.getElementById("Email").value.trim();
        
        var Medico_ID_MEDICO = document.getElementById("Medico_ID_MEDICO").value.trim();
        var Familiar_ID_FAMILIAR = document.getElementById("Familiar_ID_FAMILIAR").value.trim();
        var Direccion = document.getElementById("Direccion").value;
        var Ciudad = document.getElementById("Ciudad").value.trim();
        var Latitud = document.getElementById("Latitud").value.trim();
        var Longitud = document.getElementById("Longitud").value.trim();
        var Fecha_Nacimiento = document.getElementById("Fecha_Nacimiento").value.trim();
        
        if(!comprobarInfoBasica(identificacion,Password,Nombre,Apellido,Telefono,Genero,Email)){
            return;
        }

        if(!comprobarInfoEspecifica(Medico_ID_MEDICO, Familiar_ID_FAMILIAR, Direccion, Ciudad, Latitud, Longitud, Fecha_Nacimiento)){
            return;
        }
            
        var respuesta = confirm("Está seguro de crear el Paciente?")

        if (respuesta) {
            const data = {
                "Identificacion": identificacion,
                "Password": Password,
                "Nombre": Nombre,
                "Apellido": Apellido,
                "Telefono": Telefono,
                "Genero": Genero,
                "Email": Email,

                "Medico_ID_MEDICO" : Medico_ID_MEDICO==""?null:Medico_ID_MEDICO,
                "Familiar_ID_FAMILIAR" : Familiar_ID_FAMILIAR==""?null:Familiar_ID_FAMILIAR,
                "Direccion" : Direccion,
                "Ciudad" : Ciudad,
                "Latitud" : Latitud,
                "Longitud" : Longitud,
                "Fecha_Nacimiento" : Fecha_Nacimiento
            };
            
            const dataToSend = JSON.stringify(data);
            
            newEntidad(dataToSend);
        } else {
            alert("Proceso cancelado.");
        }
    }, 600);
}

function comprobarInfoBasica(Identificacion,Password,Nombre,Apellido,Telefono,Genero,Email){
    
    if (Identificacion === ""){
        alert("escriba su Identificacion")
        return false;
    }
    if (getPersona(Number(Identificacion,"Paciente", false))){
        alert("Ya existe Usuario")
        return false;
    }
    if (Identificacion === ""){
        alert("escriba su Identificacion")
        return false;
    }
    if (Password === ""){
        alert("escriba su Password")
        return false;
    }
    if (Nombre === ""){
        alert("escriba su Nombre")
        return false;
    }
    if (Apellido === ""){
        alert("escriba su Apellido")
        return false;
    }
    if (Telefono === ""){
        alert("escriba su Telefono")
        return false;
    }
    if (Genero === "null"){
        alert("Seleccione Genero")
        return false;
    }
    if (Email === ""){
        alert("escriba su Email")
        return false;
    }

    return true
}

function comprobarInfoEspecifica(Medico_ID_MEDICO, Familiar_ID_FAMILIAR, Direccion, Ciudad, Latitud, Longitud, Fecha_Nacimiento){
    if (Medico_ID_MEDICO != ""){
        if (!getPersona(Number(Medico_ID_MEDICO,"Médico", true))){
            alert("No existe medico con ese ID")
            return false;
        }
    }
    if (Familiar_ID_FAMILIAR != ""){
        if (!getPersona(Number(Familiar_ID_FAMILIAR,"Familiar", true))){
            alert("No existe familiar con ese ID")
            return false;
        }
    }
    if (Direccion === ""){
        alert("escriba su Direccion")
        return false;
    }
    if (Ciudad === ""){
        alert("escriba su Ciudad")
        return false;
    }
    if (Latitud === ""){
        alert("escriba su Latitud")
        return false;
    }
    if (Longitud === ""){
        alert("escriba su Longitud")
        return false;
    }
    if (Fecha_Nacimiento === ""){
        alert("escriba su Fecha de nacimiento")
        return false;
    }
    return true
}

function getUsuarios() {
    fetch(getUsuUrl)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                console.log(response.body)
                throw new Error(response.status)
            }
        })
        .then(data => {
            usuarios = JSON.parse(data);
            console.log(usuarios);
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function getPersona(Identificacion,rol,RolIgual){
    let salida = false

    usuarios.forEach((usu) => {
        if(RolIgual){
            if(usu.Identificacion==Identificacion && rol== usu.Rol ){
                salida = true
            }
        } else{
            if(usu.Identificacion==Identificacion){
                salida = true
            }
        }
    });

    console.log(salida)
    return salida
}

/* function pushMedico() {
    const select = [];
    console.log(especialidad.length);
    if (especialidad.length > 0) {

        especialidad.forEach((esp) => {
            const option = document.createElement("option");
            option.innerHTML = `<option value='${esp.id}' >${esp.id}- ${esp.Especialidad}</option>`;
            select.push(option);
        });
        const info = document.getElementById("especialidad");
        select.forEach(sel => info.appendChild(sel));
    }
} 
function pushFamiliar() {
    const select = [];
    console.log(especialidad.length);
    if (especialidad.length > 0) {

        especialidad.forEach((esp) => {
            const option = document.createElement("option");
            option.innerHTML = `<option value='${esp.id}' >${esp.id}- ${esp.Especialidad}</option>`;
            select.push(option);
        });
        const info = document.getElementById("especialidad");
        select.forEach(sel => info.appendChild(sel));
    }
}*/


function newEntidad(data) {
    fetch(newEntUrl, {
            method: "POST",
            headers: {
                "Content-Type": "text/json"
            },
            body: data
        })
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                console.log(response.body)
                throw new Error(response.status)
            }
        })
        .then(data => {
            console.log(data);
            var mess = "creado";
            RespExitosa(mess);
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function RespExitosa(mess) {
    alert("Paciente " + mess + " exitosamente!!");
    location.reload();
}