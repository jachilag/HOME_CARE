
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const newEntUrl = host + 'nuevoFamiliar';
const getFamUrl = host + 'getFamiliar';
let usuarios = [];
let usuario = [];

function create() {
    var identificacion = document.getElementById("Identificacion").value.trim();
    var Password = document.getElementById("Password").value.trim();
    var Nombre = document.getElementById("Nombre").value.trim();
    var Apellido = document.getElementById("Apellido").value.trim();
    var Telefono = document.getElementById("Telefono").value.trim();
    var Genero = document.getElementById("Genero").value.trim();
    var Email = document.getElementById("Email").value.trim();
    
    var Parentesco = document.getElementById("Parentesco").value;
    
    
    if(!comprobarInfoBasica(identificacion,Password,Nombre,Apellido,Telefono,Genero,Email)){
        return;
    }

    if(!comprobarInfoEspecifica(Parentesco)){
        return;
    }
    
    var respuesta = confirm("Está seguro de crear el Familiar?")
    if (respuesta) {
        const data = {
            "Identificacion": identificacion,
            "Password": Password,
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Telefono": Telefono,
            "Genero": Genero,
            "Email": Email,

            "parentesco" : Parentesco
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

function comprobarInfoEspecifica(Parentesco){
    if (Parentesco === ""){
        alert("escriba su Parentesco")
        return false;
    }
    return true
}

function validar() {
    var id = document.getElementById("Identificacion").value.trim();
    validate(getFamUrl, id, ()=>{alert( "Ya hay un Familiar con ese ID")}, create)    
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
            RespExitosa("creado");
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function RespExitosa(mess) {
    alert("Familiar " + mess + " exitosamente!!");
    location.reload();
}

function nada(){}