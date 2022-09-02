CREATE SCHEMA BD_HOME_CARE;
USE BD_HOME_CARE;

CREATE TABLE Signos_vitales(
    ID_SIGNO_VITAL INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    Tipo_Signo CHAR(60) INT NOT NULL
    );

CREATE TABLE Rol(
	ID_ROL INT NOT NULL,
	Rol varchar(60) NOT NULL
);

CREATE TABLE Persona(
    ID_PERSONA INT PRIMARY KEY AUTO_INCREMENT NOT NULL ,
    Identificacion VARCHAR(60) NOT NULL,
    Apellido  VARCHAR(60) NOT NULL,
    Telefono VARCHAR(60) NOT NULL,
    Genero VARCHAR(60) NOT NULL,
    Email VARCHAR(60) NOT NULL
    ID_ROL INT NOT NULL,
    FOREIGN KEY ID_ROL REFERENCES Rol(ID_ROL)
);

CREATE TABLE Usuarios(
	ID_LOGIN INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	ID_ROL INT NOT NULL,
	Identificacion VARCHAR(60) NOT NULL,
	Contraseña varchar(60) NOT NULL,
	FOREIGN KEY (ID_ROL) REFERENCES Rol(ID_ROL),
    FOREIGN KEY (Identificacion) REFERENCES Persona(Identificacion)
);

CREATE TABLE Enfermero{
    ID_ENFERMERO INT PRIMARY KEY AUTO_INCREMENT NOT NULL
    ID_PERSONA INT NOT NULL
    FOREIGN KEY ID_PERSONA REFERENCES persona(ID_PERSONA)
};

CREATE TABLE Auxiliar{
    ID_AUXILIAR INT PRIMARY KEY NOT NULL
    ID_PERSONA INT NOT NULL
    FOREIGN KEY ID_PERSONA REFERENCES persona(ID_PERSONA)
};

CREATE TABLE Familiar{
    ID_FAMILIAR INT PRIMARY AUTO_INCREMENT KEY NOT NULL,
    parentesco VARCHAR(60) NOT NULL
    ID_PERSONA INT NOT NULL
    FOREIGN KEY ID_PERSONA REFERENCES persona(ID_PERSONA)
};


CREATE TABLE Paciente (
    ID_PACIENTE INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    Persona_ID_PERSONA INT NOT NULL,
    Medico_ID_MEDICO INT NOT NULL,
    Familiar_ID_FAMILIAR INT NOT NULL,
    Direccion CHAR(255) NOT NULL,
    Ciudad CHAR(60) INT NOT NULL,
    Latitud DECIMAL(6,5) INT NOT NULL,
    Longitud DECIMAL(6,5) INT NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    FOREIGN KEY (Persona_ID_PERSONA) REFERENCES Persona(ID_PERSONA),     
    FOREIGN KEY (Medico_ID_MEDICO) REFERENCES Medico(ID_MEDICO),
    FOREIGN KEY (Familiar_ID_FAMILIAR) REFERENCES Familiar(ID_FAMILIAR)
);

CREATE TABLE Registro_SV(
    ID_REGISTRO_SV BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    SV_ID_SIGNO_VITAL INT NOT NULL,
    Paciente_ID_PACIENTE INT NOT NULL,
    Medida DECIMAL(6,3) NOT NULL,
    Fecha_Hora DATETIME NOT NULL,
    FOREIGN KEY (SV_ID_SIGNO_VITAL) REFERENCES Signos_vitales(ID_SIGNO_VITAL),
    FOREIGN KEY (Paciente_ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE)
);

CREATE TABLE Registro_SV(
    ID_REGISTRO_SV BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    SV_ID_SIGNO_VITAL INT NOT NULL,
    Paciente_ID_PACIENTE INT NOT NULL,
    Medida DECIMAL(6,3) NOT NULL,
    Fecha_Hora DATETIME NOT NULL,
    FOREIGN KEY (SV_ID_SIGNO_VITAL) REFERENCES Signos_vitales(ID_SIGNO_VITAL),
    FOREIGN KEY (Paciente_ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE)
    );

