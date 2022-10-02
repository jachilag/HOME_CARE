//------------------------------------------------------Consulta Usuario
const queri_url = 'https://home-care-db-2022-g7.herokuapp.com/getPersona/';
let user_information = [];
//----------------------------------------------Realiza peticion
function getPersona(queri_url) {
    let identificacion = document.formulario__consulta.Identificacion.value;
    let final_queri_url = queri_url + identificacion;
    
    fetch(final_queri_url)
        .then(response => {
            if(response.ok ){
                return response.text()
            }else{
                
                throw new Error(response.status)
            }
        })
        .then(data =>{
            user_information = JSON.parse(data);
            handlerSuccess();
        })
        .catch (error=> {
            console.log("Error"+ error);
            handlerError();
        });
}
document.getElementById('consulta_btn').addEventListener('click', () => getPersona(queri_url));
//-------------------------------Compara cabeceras y llena el formulario.
function handlerSuccess() {
        [...document.getElementById('usuario_formulario')].forEach((form_element) => {
            Object.keys(user_information).forEach((user_element)=> {
                if (form_element.getAttribute("name") == user_element){
                    form_element.value = user_information[user_element];
                }
            })    
        })
}
function handlerError() {
    document.getElementById('usuario_formulario').remove();
    const div_user_form = document.getElementById('usuario__informacion');
    const new_h = document.createElement('h1');
    new_h.setAttribute('id','Alert')
    new_h.style.height = '500px';
    new_h.style.textAlign = 'center';
    new_h.textContent = "No se encontro usuario";
    div_user_form.appendChild(new_h);
}