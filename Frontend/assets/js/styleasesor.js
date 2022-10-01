//Ejecutar botones
document.getElementById("btn__registrate").addEventListener("click", register);
document.getElementById("btn__consultar").addEventListener("click", consulta);

//declaramos las variables
var contenedor_consulta_register = document.querySelector('.contenedor__consulta-register');
var formulario_consulta = document.querySelector('.formulario__consulta');
var formulario_register = document.querySelector('.formulario__register');
var caja_trasera_consulta = document.querySelector('.caja_trasera-consulta');
var caja_trasera_register = document.querySelector('.caja_trasera-register');

function register() {


    formulario_register.style.display = 'block';
    contenedor_consulta_register.style.left = "500px";
    formulario_consulta.style.display = 'none';
    caja_trasera_register.style.opacity = '0';
    caja_trasera_consulta.style.opacity = '1';

}
function consulta() {

    formulario_register.style.display = 'none';
    contenedor_consulta_register.style.left = "10px";
    formulario_consulta.style.display = 'block';
    caja_trasera_register.style.opacity = '1';


}