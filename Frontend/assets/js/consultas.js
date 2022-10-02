//Queri infomation of people.

const queri_url = 'https://home-care-db-2022-g7.herokuapp.com/getPersona/';
const user_form = document.getElementById('formulario__consulta');
const queri_btn = user_form.childNodes[5];
const close_btn = document.getElementById('usr_form_close');
const modal_form = document.getElementById('usuario_formulario');
let user_information = [];

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
            
            fillUserinfo();
        })
        .catch (error=> {
            console.log("Error"+ error);
            alert("No se encontro Usuario");
        });
}
//Compara cabeceras y llena el formulario.
function fillUserinfo() {
    let modal_user_form = document.getElementById('usuario__informacion');
        [...modal_user_form.childNodes[1]].forEach((form_element) => {
            Object.keys(user_information).forEach((user_element)=> {
                if (form_element.getAttribute("name") == user_element){
                    form_element.value = user_information[user_element];
                }
            })    
        })
}
//Llama al formulario y consulta datos
queri_btn.addEventListener('click', () => getPersona(queri_url));
//Limpia el formulario
close_btn.addEventListener('click', () => {
    let modal_user_form = document.getElementById('usuario__informacion');
    [...modal_user_form.childNodes[1]].forEach((form_element) => {
        form_element.value = ""
    });
})




/*//Ocultar formulario
//function hideForm() {
    let modal = document.getElementById('usuario');
    let body = document.getElementById('body');
    body.removeChild(body.childNodes.length);
    body.removeAttribute('class');
    body.removeAttribute('style');
    modal.setAttribute('class', 'modal');
    modal.setAttribute('style',"display: none;");
    modal.removeAttribute('role');
    modal.setAttribute('aria-hidden',"true");}
*/
// Muestra el formulario
//function showForm(){
    /*
    let modal = document.getElementById('usuario');
    let body = document.getElementById('body');
    let div =  document.createElement('div');
    body.setAttribute('class','modal-open');
    body.setAttribute('style', 'overflow: hidden; padding-right: 0px;');
    div.setAttribute('class',"modal-backdrop show")
    div.setAttribute('id',"div_modal_final")
    modal.setAttribute('class', 'modal show');
    modal.setAttribute('style',"display: block;");
    modal.setAttribute('role' , 'dialog');*/
//}