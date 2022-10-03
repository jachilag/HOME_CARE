
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const parsedUrl = new URL(window.location.href);
const userId = parsedUrl.searchParams.get("id");
const getMedUrl = host + 'getPersona';
const getPerUrl = host + 'getPersonas';
const getPacUrl = host + 'getMisPacientes';
let MisPacientes = [];
let personas = [];
let usuario = [];

function getDatosInicio() {
    fetch(getMedUrl + '/' + userId)
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
            getMisPacientes();
        })
        .catch(err => {
            console.log("Error: " + err);
    });
}

function pushDatosInicio() {
    document.getElementById("Identificacion").innerHTML = usuario.Identificacion;
    document.getElementById("Medico").innerHTML = usuario.Nombre;
}


// ================================================================================================
function getMisPacientes() {
    fetch(getPacUrl+'/'+userId)
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            MisPacientes = JSON.parse(data);
            console.log(MisPacientes);
            pullPac();
        })
        .catch(err => {
            console.log("Error: " + err);
    });
}

function pullPac() {
    const table = [];
    console.log(MisPacientes.length);
    if (MisPacientes.length > 0) {
        MisPacientes.forEach((pac) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `<tr><td>${pac.Identificacion}</td><td>${pac.Nombre}</td><td>${pac.Apellido}</td><td>${pac.Genero}</td><td>${pac.Telefono}</td><td>${pac.Fecha_Nacimiento}</td></tr>`;
            table.push(tr);
        });
        const info = document.getElementById("tableall");
        table.forEach(tr => info.appendChild(tr));
    }
}

document.addEventListener("DOMContentLoaded", getDatosInicio);
