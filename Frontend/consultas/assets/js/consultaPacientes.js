// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const getPacUrl = host + 'getPacientes';
const getPacIndUrl = host + 'getPaciente';
let MisPacientes = [];
PacInd = [];


function getPacientes() {
    fetch(getPacUrl)
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
        // document.getElementById("notFound").remove();

        MisPacientes.forEach((pac) => {
            const tr = document.createElement("tr");
            // tr.innerHTML = `<tr><td>${pac.Identificacion}</td><td>${pac.Medico_ID_MEDICO}</td><td><i class="bi bi-pencil" onclick='showModal(${esp.id}, "${esp.Especialidad}")'></i></td><td><i class="bi bi-trash3" onclick='showModalEli(${esp.id}, "${esp.Especialidad}")'></i></td></tr>`;
            tr.innerHTML = `<tr><td>${pac.Identificacion}</td><td>${pac.Nombre}</td><td>${pac.Apellido}</td><td>${pac.Telefono}</td><td>${pac.Direccion}</td></tr>`;
            table.push(tr);
        });
        const info = document.getElementById("tableall");
        table.forEach(tr => info.appendChild(tr));
    }
}


function validate() {
    var id = document.getElementById('identificacion').value;
    console.log(id);

    if (id == '' || id == undefined) {
        alert('Debe diligenciar un valor válido para la identificación del paciente!!!');
    } else {
        var search = document.getElementById('search');
        search.style.display = 'none';

        var result = document.getElementById('result');
        result.style.display = 'block';

        fetch(getPacIndUrl + '/' + id)
            .then(response => {
                if (response.ok) {
                    return response.text()
                } else {
                    throw new Error(response.status)
                }
            })
            .then(data => {
                PacInd = JSON.parse(data);
                console.log(PacInd);
                fillData();
            })
            .catch(err => {
                console.log("Error: " + err);
            });

    }
}

function fillData() {
    document.getElementById('ide').innerHTML = PacInd.Identificacion;
    document.getElementById('Medico_ID_MEDICO').innerHTML = PacInd.Medico_ID_MEDICO;
    document.getElementById('Familiar_ID_FAMILIAR').innerHTML = PacInd.Familiar_ID_FAMILIAR;
    document.getElementById('Nombre').innerHTML = PacInd.Nombre;
    document.getElementById('Apellido').innerHTML = PacInd.Apellido;
    document.getElementById('Genero').innerHTML = PacInd.Genero;
    document.getElementById('Telefono').innerHTML = PacInd.Telefono;
    document.getElementById('Fecha_Nacimiento').innerHTML = PacInd.Fecha_Nacimiento;
    document.getElementById('Direccion').innerHTML = PacInd.Direccion;
    document.getElementById('Ciudad').innerHTML = PacInd.Ciudad;
    document.getElementById('Latitud').innerHTML = PacInd.Latitud;
    document.getElementById('Longitud').innerHTML = PacInd.Longitud;
}

document.addEventListener("DOMContentLoaded", getPacientes);
