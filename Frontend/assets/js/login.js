const login_url = 'https://home-care-db-2022-g7.herokuapp.com/login';
const rol_url = 'https://home-care-db-2022-g7.herokuapp.com/getRol/';
const login_btn = document.getElementById('ingresar');

function getInfo() {
    const login_user = document.getElementById('usuario').value;
    const login_pass = document.getElementById('Contrasena').value;
    const login_role = document.getElementById('role_input').value;
    const user_info = {
        Identificacion: login_user,
        Password: login_pass,
        ID_ROL: login_role
    }
    const dataLogin = JSON.stringify(user_info);
    login(dataLogin);
}

function login(data){
    fetch(login_url, {
        method: "POST",
        headers: {"Content-Type": "text/json"}
    })
        .then(response => {
            if(response.ok ){
                return response.text()
            }
        })
        .then(data =>{
            console.log(data)
            handlerSuccess();
        })
        .catch (error=> {
            console.log("Error"+ error)
            handlerError();
        });
    }

function handlerSuccess(){
        document.getElementById('main').remove();
        const respuesta = document.createElement('p');
        respuesta.innerHTML = "Acceso Exitoso";
        const body = document.getElementById('body');
        body.appendChild(respuesta);
}

function handlerError(){
    document.getElementById('main').remove();
    const respuesta = document.createElement('p');
    respuesta.innerHTML = "No se encontro usuario";
    const body = document.getElementById('body');
    body.appendChild(respuesta);
}
login_btn.addEventListener('click', () => {getInfo()});
