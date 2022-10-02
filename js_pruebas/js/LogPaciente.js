
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
}

function misDatos(){
    // sessionStorage.setItem('userID', userId)
    window.location.href = './ModifyPaciente.html?id=' + userId;
}

function Registrar_SV(){
    window.location.href = './Registrar_SV.html?id=' + userId;
}


document.addEventListener("DOMContentLoaded", getDatosInicio);