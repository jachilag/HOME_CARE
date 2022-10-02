
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const parsedUrl = new URL(window.location.href);
const userId = parsedUrl.searchParams.get("id");
const getPerUrl = host + 'getPersona';
let usuario = [];

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
            pushDatosInicio();
        })
        .catch(err => {
            console.log("Error: " + err);
    });
}

function pushDatosInicio() {
    document.getElementById("Identificacion").innerHTML = usuario.Identificacion;
    document.getElementById("Nombre").innerHTML = usuario.Nombre;
    document.getElementById("tel").innerHTML = usuario.Telefono;
    document.getElementById("ema").innerHTML = usuario.Email;
}



function comprobarInfoBasica(Password,Telefono,Email){
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

    const medico = {
        Password : pas,
        Telefono : (tel == '' || tel == undefined)?usuario.Telefono:tel,
        Email : (ema == '' || ema == undefined)?usuario.Email:ema,

    }
    
    const dataMedico = JSON.stringify(medico);
    console.log(dataMedico)
    updateData(host+'updateMedico', userId, dataMedico, 'no se actualizon datos', ()=>{alert("datos actualizados");getDatosInicio()},nada)
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
