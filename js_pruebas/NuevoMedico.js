
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const getEspUrl = host + 'getEspecialidades';
const newMedUrl = host + 'nuevoMedico';
let Esp = [];


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
            Esp = JSON.parse(data);
            console.log(Esp);
            pullEsp();
        })
        .catch(err => {
            console.log("Error: " + err);
        });
}

function pullEsp() {
    const select = [];
    console.log(Esp.length);
    if (Esp.length > 0) {

        Esp.forEach((esp) => {
            const option = document.createElement("option");
            option.innerHTML = `<option value='${esp.id}' >${esp.id}- ${esp.Especialidad}</option>`;
            select.push(option);
        });
        const info = document.getElementById("espe");
        select.forEach(sel => info.appendChild(sel));
    }
}







function create() {
    var id = document.getElementById("Identificacion").value;
    var Password = document.getElementById("Password").value;
    var Nombre = document.getElementById("Nombre").value;
    var Apellido = document.getElementById("Apellido").value;
    var Telefono = document.getElementById("Telefono").value;
    var Genero = document.getElementById("Genero").value;
    var Email = document.getElementById("Email").value;
    var esp = document.getElementById("espe").value;
    var espe = esp.split('-');
    var Registro = document.getElementById("Registro").value;

    // alert(`${id}  ${Password}  ${Nombre} ${Apellido} ${Telefono} ${Genero} ${Email} ${espe[0].toString()} ${Registro}`);

    // if (id == "" || id == undefined || Password == "" || Password == undefined || nombre == "" || nombre == undefined || Apellido == "" || Apellido == undefined ||
    //     Telefono == "" || Telefono == undefined) {

    // }


    // if (newesp == "" || newesp == undefined) {
    //     alert("Por favor ingrese un valor");
    // } else {
    var respuesta = confirm("Está seguro de crear el Medico?")

    if (respuesta) {
        const data = {
            "Identificacion": id,
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
        // alert(dataToSend);

        newMed(dataToSend);
    } else {
        alert("Proceso cancelado.");
    }
    // }
}

// function cambiar() {
//     var select = document.getElementById("espe"), //El <select>
//         value = select.value, //El valor seleccionado
//         text = select.options[select.selectedIndex].innerText; //El texto de la opción seleccionada
//     alert(`${value}   ${text}`)
// }

// /función para crear la especialidad
function newMed(data) {
    fetch(newMedUrl, {
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

document.addEventListener("DOMContentLoaded", getEspecialidades);
