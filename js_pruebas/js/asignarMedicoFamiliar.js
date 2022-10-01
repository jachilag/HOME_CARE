
// const host = 'http://127.0.0.1:8000/';
const host = 'https://home-care-db-2022-g7.herokuapp.com/';

const getPacUrl = host + 'getPaciente';
const getMedUrl = host + 'getMedico';
const getFamUrl = host + 'getFamiliar';
const updMedUrl = host + 'updatePaciente_Medico';
const updFamUrl = host + 'updatePaciente_Familiar';
const userId = sessionStorage.getItem('clientId');

let usuario = [];

function RespExitosa(mess) {
    alert("Paciente " + mess + " exitosamente!!");
    location.reload();
}

function validar_familiar(Familiar_ID_FAMILIAR) {
    if (Familiar_ID_FAMILIAR != ""){
        if (!getPersona(Number(Familiar_ID_FAMILIAR,"Familiar", true))){
            return false;
        }
    }
}

function consultar() {
    var id = document.getElementById('Identificacion').value.trim();
    if (id == '' || id == undefined) {
        alert("digite Identificacion")
    } else {
        validate(getPacUrl, id, "No existe Paciente con ese ID", fillData, () => {
            document.getElementById('consultaMedico').innerHTML = "";
            document.getElementById('consultaFamiliar').innerHTML = "";
        })    
    }
}

function fillData() {
    familiar = usuario.Familiar_ID_FAMILIAR==null?'No asignado':usuario.Familiar_ID_FAMILIAR
    medico = usuario.Medico_ID_MEDICO==null?'No asignado':usuario.Medico_ID_MEDICO
    document.getElementById('consultaMedico').innerHTML = medico;
    document.getElementById('consultaFamiliar').innerHTML = familiar;
}

function actualizar() {
    validar_paciente();
}

function validar_paciente() {
    var id = document.getElementById("Identificacion").value.trim();
    validate(getPacUrl, id, "No existe Paciente con ese ID", validar_medico, nada)    
}

function validar_medico() {
    var id = document.getElementById("Medico_ID_MEDICO").value.trim();
    if (id == '' || id == undefined) {
        validar_familiar()
    } else {
        validate(getMedUrl, id, "No existe Medico con ese ID", validar_familiar,nada)    
    }
}

function validar_familiar() {
    var id = document.getElementById("Familiar_ID_FAMILIAR").value.trim();
    if (id == '' || id == undefined) {
        sendData()
    } else {
        validate(getFamUrl, id, "No existe Familiar con ese ID", sendData,nada)    
    }
}

function sendData(){
    var id_paciente = document.getElementById("Identificacion").value.trim();
    var id_medico = document.getElementById("Medico_ID_MEDICO").value.trim();
    var id_familiar = document.getElementById("Familiar_ID_FAMILIAR").value.trim();

    const medico = {
        Medico_ID_MEDICO : (id_medico == '' || id_medico == undefined)?null:id_medico
    }
    const familiar = {
        Familiar_ID_FAMILIAR : (id_familiar == '' || id_familiar == undefined)?null:id_familiar
    }
    
    const dataMedico = JSON.stringify(medico);
    const dataFamiliar = JSON.stringify(familiar);
    updateData(updMedUrl, id_paciente, dataMedico, 'no se actualizo el medico asignado', nada,nada)
    updateData(updFamUrl, id_paciente, dataFamiliar, 'no se actualizo el familiar asignado', ()=>{alert("datos actualizados")},nada)
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

function validate(url, id, textError, func, funcNot) {

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
            alert(textError)
            funcNot()
            console.log("Error: " + err);
        });
}

function nada(){}

