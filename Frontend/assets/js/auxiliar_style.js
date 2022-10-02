//Ejecutar botones
document.getElementById("btn__registrate").addEventListener("click", register);
document.getElementById("btn__consultar").addEventListener("click", consulta);
document.getElementById('usr_form_close').addEventListener('click', clearForm);
document.getElementById('usr_form_x_btn').addEventListener('click', clearForm);

//declaramos las variables
var contenedor_consulta_register = document.querySelector('.contenedor__consulta-register');
var formulario_consulta = document.querySelector('.formulario__consulta');
var formulario_register = document.querySelector('.formulario__register');
var caja_trasera_consulta = document.querySelector('.caja_trasera-consulta');
var caja_trasera_register = document.querySelector('.caja_trasera-register');
const formulario_constulta = document.getElementById('usuario_formulario');

//---------------Habilita la caja registro---------------------
function register() {
    formulario_register.style.display = 'block';
    contenedor_consulta_register.style.left = "500px";
    formulario_consulta.style.display = 'none';
    caja_trasera_register.style.opacity = '0';
    caja_trasera_consulta.style.opacity = '1';
}
//---------------Habilita la caja consulta---------------------
function consulta() {
    formulario_register.style.display = 'none';
    contenedor_consulta_register.style.left = "10px";
    formulario_consulta.style.display = 'block';
    caja_trasera_register.style.opacity = '1';
}
//-------------------Limpia el formulario Consulta---------------------------
function clearForm() {
    if(document.getElementById('usuario_formulario') != null){
    [...document.getElementById('usuario_formulario')].forEach((form_element) => {
        form_element.value = ""
    });} else{
        const div_user_form = document.getElementById('usuario__informacion');
        document.getElementById('Alert').remove();
        div_user_form.appendChild(formulario_constulta);
    }
}