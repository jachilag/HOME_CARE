
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const parsedUrl = new URL(window.location.href);
const userId = parsedUrl.searchParams.get("id");
const getPerUrl = host + 'getPersona';
const getSigUrl = host + 'getSignos';
const newEntUrl = host + 'nuevoRegistro_SV';
let usuario = [];
let signo = [];

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
    getSV();
}

function misPacientes() {
    // sessionStorage.setItem('userID', userId)
    window.location.href = './MisPacientes.html?id=' + userId;
}

function misDatos() {
    // sessionStorage.setItem('userID', userId)
    window.location.href = './ModifyMedico.html?id=' + userId;
}

function getSV() {
    fetch(getSigUrl)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            signo = JSON.parse(data);
            pushSV();
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function pushSV() {
    const select = [];
    if (signo.length > 0) {

        signo.forEach((sig) => {
            const option = document.createElement("option");
            option.innerHTML = `<option value='${sig.id}' >${sig.id}- ${sig.Signo}</option>`;
            select.push(option);
        });
        const info = document.getElementById("SignoVital");
        select.forEach(sel => info.appendChild(sel));
    }
}

function create() {
    var sig = document.getElementById("SignoVital").value.trim();
    var med = document.getElementById("Medida").value.trim();
    var signo = sig.split('-');

    if(med==undefined){alert("medida no puede ser vacia");return;}
    const data = {
        "SV_ID_SIGNO_VITAL": parseInt(signo[0]),
        "Identificacion": Number(userId),
        "Medida": Number(med)
    };
    const dataToSend = JSON.stringify(data);
    console.log(dataToSend)
    newEntidad(dataToSend);
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
            var mess = "Registrado";
            RespExitosa(mess);
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function RespExitosa(mess) {
    alert("Signo Vital " + mess + " exitosamente!!");
    location.reload();
}

document.addEventListener("DOMContentLoaded", getDatosInicio);
