//Queri infomation of people.

const queri_url = 'https://home-care-db-2022-g7.herokuapp.com/getPersona/';
const user_form = document.getElementById('formulario__consulta');
const queri_btn = user_form.childNodes[5];
const close_btn = document.getElementById('usr_form_close');
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
            queri_btn.setAttribute("data-bs-toggle","modal");
            queri_btn.setAttribute("data-bs-target","#usuario");
            fillUserinfo();
        })
        .catch (error=> {
        });
}
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
queri_btn.addEventListener('click', () => getPersona(queri_url));
close_btn.addEventListener(('click'), ()=> {
    queri_btn.removeAttribute("data-bs-toggle","modal");
    queri_btn.removeAttribute("data-bs-target","#usuario");
})