const login_url = 'https://home-care-db-2022-g7.herokuapp.com/login';
const rol_url = 'https://home-care-db-2022-g7.herokuapp.com/getRol/';
const login_btn = document.getElementById('ingresar');
// ------------------------Captura la informacion del formulario ----------
function getInfo() {
    const login_user = document.getElementById('usuario').value;
    const login_pass = document.getElementById('Contrasena').value;
    const login_rol = document.getElementById('datalist_id').value;

    const user_info = {
        Identificacion: login_user,
        Password: login_pass,
        ID_ROL: login_rol
    }
    //Convierte los datos a JSON.
    const dataLogin = JSON.stringify(user_info);
    login(dataLogin);
}
// --------------------- Realiza una promesa con Fetch para peticion POST
function login(data) {
    fetch(login_url, {
        method: "POST",
        headers: { "Content-Type": "text/json" },
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
            console.log(data.Identificacion)
            handlerSuccess();
        })
        .catch(error => {
            console.log("Error" + error);
            handlerError();
        });
}
login_btn.addEventListener('click', () => { getInfo() });
// -----------------------------------------Alerta Acceso Exitoso.
function handlerSuccess() {
    const respuesta = document.createElement('h1');
    document.getElementById('login').remove();
    respuesta.innerHTML = "Acceso Exitoso";
    const div_main = document.getElementById('contenedor_formulario');
    div_main.appendChild(respuesta);
}
//------------------------------Muestra alerta de datos invalidos.
function handlerError() {
    const form = document.getElementById('login');
    const respuesta = document.createElement('p');
    // Estilo de la alerta
    if (document.getElementById('acceso_fallido') == null) {
        respuesta.setAttribute('id', 'acceso_fallido');
        respuesta.innerHTML = "Acceso fallido: Usuario, Contraseña o Rol Invalido";
        respuesta.style.marginLeft = "25px";
        respuesta.style.fontSize = "x-large";
        respuesta.style.textAlign = "center";
        respuesta.style.color = "red";
        respuesta.style.borderColor = "red";
        respuesta.style.borderStyle = 'solid';
        respuesta.style.borderRadius = "20px";
        const btn = document.getElementById('ingresar');
        form.insertBefore(respuesta, btn);
    }
    else {
        setTimeout(() => {
            document.getElementById('acceso_fallido').style.borderColor = 'red';
            document.getElementById('acceso_fallido').style.borderStyle = 'solid';
        }
            , 100);
        document.getElementById('acceso_fallido').style.borderStyle = 'hidden';
    }
}

