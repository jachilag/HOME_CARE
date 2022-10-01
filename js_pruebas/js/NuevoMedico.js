
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const newEntUrl = host + 'nuevoMedico';
const getEspUrl = host + 'getEspecialidades';
const getPacUrl = host + 'getPaciente';
const getMedUrl = host + 'getMedico';
const getFamUrl = host + 'getFamiliar';
let usuario = [];
let especialidad = [];
let usuarios = [];


function getEspecialidades() {
    fetch(getEspUrl)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            especialidad = JSON.parse(data);
            console.log(especialidad);
            pushEspecialidad();
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function pushEspecialidad() {
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

function create() {
    var Identificacion = document.getElementById("Identificacion").value.trim();
    var Password = document.getElementById("Password").value.trim();
    var Nombre = document.getElementById("Nombre").value.trim();
    var Apellido = document.getElementById("Apellido").value.trim();
    var Telefono = document.getElementById("Telefono").value.trim();
    var Genero = document.getElementById("Genero").value.trim();
    var Email = document.getElementById("Email").value.trim();

    var esp = document.getElementById("especialidad").value;
    var espe = esp.split('-');
    var Registro = document.getElementById("Registro").value.trim();

    if(!comprobarInfoBasica(Identificacion,Password,Nombre,Apellido,Telefono,Genero,Email)){
        return;
    }

    if(!comprobarInfoEspecifica(Registro)){
        return;
    }
    
    var respuesta = confirm("Está seguro de crear el Medico?")

    if (respuesta) {
        const data = {
            "Identificacion": Identificacion,
            "Password": Password,
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Telefono": Telefono,
            "Genero": Genero,
            "Email": Email,
            "ID_ESPECIALIDAD": parseInt(espe[0]),
            "Registro": Registro
        };
        const dataToSend = JSON.stringify(data);
        newEntidad(dataToSend);
    } else {
        alert("Proceso cancelado.");
    }

}

function comprobarInfoBasica(Identificacion,Password,Nombre,Apellido,Telefono,Genero,Email){
    
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

function comprobarInfoEspecifica(Registro){
    if (Registro === ""){
        alert("escriba el Registro profesional")
        return false;
    }
    return true
}

function validar() {
    var id = document.getElementById("Identificacion").value.trim();
    validate(getMedUrl, id, ()=>{alert( "Ya hay un Medico con ese ID")}, create)    
}

// /función para crear un medico
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
    alert("Medico " + mess + " exitosamente!!");
    location.reload();
}

function validate(url, id, func, funcNot) {

    fetch(url + '/' + Number(id))
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            usuario = JSON.parse(data);
            func();
        })
        .catch(err => {
            funcNot()
            console.log("Error: " + err);
    });
}


document.addEventListener("DOMContentLoaded", getEspecialidades);
