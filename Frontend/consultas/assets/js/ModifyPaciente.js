
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const parsedUrl = new URL(window.location.href);
const userId = parsedUrl.searchParams.get("id");
const getPerUrl = host + 'getPersona';
const getPacUrl = host + 'getPaciente';
let usuario = [];
let paciente = [];


function getDatosInicio() {
    fetch(getPerUrl + '/' + userId)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            usuario = JSON.parse(data);
            getDatosPaciente();
        })
        .catch(err => {
            console.log("Error: " + err);
    });
}
function getDatosPaciente() {
    fetch(getPacUrl + '/' + userId)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            paciente = JSON.parse(data);
            console.log(paciente)
            pushDatosInicio();
        })
        .catch(err => {
            console.log("Error: " + err);
    });
}

function misDatos(){
    // sessionStorage.setItem('userID', userId)
    window.location.href = 'paciente.html?id=' + userId;
}

function Registrar_SV(){
    window.location.href = 'registrosv.html?id=' + userId;
}
function pushDatosInicio() {
    document.getElementById("Identificacion").innerHTML = usuario.Identificacion;
    document.getElementById("Nombre").innerHTML = usuario.Nombre;
    document.getElementById("tel").innerHTML = usuario.Telefono;
    document.getElementById("ema").innerHTML = usuario.Email;
    document.getElementById("dir").innerHTML = paciente.Direccion;
    document.getElementById("ciu").innerHTML = paciente.Ciudad;
    document.getElementById("lati").innerHTML = paciente.Latitud;
    document.getElementById("longi").innerHTML = paciente.Longitud;
}



function comprobarInfoBasica(Password,Telefono,Email,Direccion,Ciudad,Latitud,Longitud){
    if (Password === ""){
        alert("escriba su Password")
        return false;
    }
    if (Telefono === ""){
        alert("escriba su Telefono")
        return false;
    }
    if (Email === ""){
        alert("escriba su Email")
        return false;
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
    return true
}

function validar() {
    if(!comprobarInfoBasica()){
        return;
    } 
    sendData();

}

function sendData(){
    var pas = document.getElementById("Password").value.trim();
    var tel = document.getElementById("Telefono").value.trim();
    var ema = document.getElementById("Email").value.trim();
    var dir = document.getElementById("Direccion").value.trim();
    var ciu = document.getElementById("Ciudad").value.trim();
    var lati = document.getElementById("Latitud").value.trim();
    var longi = document.getElementById("Longitud").value.trim();

    const paciente = {
        Password : pas,
        Telefono : (tel == '' || tel == undefined)?usuario.Telefono:tel,
        Email : (ema == '' || ema == undefined)?usuario.Email:ema,

        Direccion : (dir == '' || dir == undefined)?paciente.Direccion:dir,
        Ciudad : (ciu == '' || ciu == undefined)?paciente.Ciudad:ciu,
        Latitud : (lati == '' || lati == undefined)?paciente.Latitud:lati,
        Longitud : (longi == '' || longi == undefined)?paciente.Longitud:longi
    }
    
    const dataPaciente = JSON.stringify(paciente);
    console.log(dataPaciente)
    updateData(host+'updatePaciente', userId, dataPaciente, 'no se actualizon datos', ()=>{alert("datos actualizados");getDatosInicio()},nada)
}

function updateData(url, id, data, textError, func, funcNot) {

    fetch(url + '/' + Number(id), {
        method: "PUT",
        headers: {
            "Content-Type": "text/json",
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
            func();
        })
        .catch(err => {
            console.log("Error: " + err);
            alert(textError)
            funcNot();
        });
}

function nada(){}

document.addEventListener("DOMContentLoaded", getDatosInicio);
