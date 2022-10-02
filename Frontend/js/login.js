
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const getUsuUrl = host + 'login';
let usuario = [];
let data = [];

function validar() {
    var Identificacion = document.getElementById("Identificacion").value.trim();
    var Password = document.getElementById("Password").value.trim();
    var Rol = document.getElementById("Rol").value.trim();

    data = {
        "ID_ROL" : Number(Rol),
        "Identificacion": Number(Identificacion),
        "Password": Password
    };
    dataToSend = JSON.stringify(data);
    solicitar(dataToSend)
}

function solicitar(dataToSend) {
    fetch(getUsuUrl, {
        method: "POST",
        headers: {
            "Content-Type": "text/json"
        },
        body: dataToSend
    })
    .then(response => {
        if (response.ok) {
            return response.text()
        } else {
            throw new Error(response.status)
        }
    })
    .then(data => {
        usuario = JSON.parse(data);
        alert("Acceso Correcto")
        handleSuccess();
    })
    .catch(err => {
        alert("datos incorrectos")
        console.log("Error: " + err);
    });
}

function handleSuccess() {
    sessionStorage.setItem('userID', data.Identificacion)

    switch (Number(data.ID_ROL)) {
        case 1:
            window.location.href = './LogMedico.html?id=' + data.Identificacion;
          break;
        case 2:
            window.location.href = './auxiliar.html?id=' + data.Identificacion;
          break;
        case 3:
            window.location.href = './LogPaciente.html?id=' + data.Identificacion;
          break;
        case 4:
            window.location.href = './LogFamiliar.html?id=' + data.Identificacion;
          break;
        default:
            location.reload();
      }   
}