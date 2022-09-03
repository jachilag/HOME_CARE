CREATE SCHEMA BD_HOME_CARE;
USE BD_HOME_CARE;

CREATE TABLE Signos_vitales(
    ID_SIGNO_VITAL SERIAL NOT NULL PRIMARY KEY, 
    Tipo_Signo CHAR(60) INT NOT NULL
);

CREATE TABLE Rol(
	ID_ROL INT NOT NULL,
	Rol varchar(60) NOT NULL
);

CREATE TABLE Persona(
    ID_PERSONA SERIAL NOT NULL PRIMARY KEY,
    Identificacion VARCHAR(60) NOT NULL,
    Apellido  VARCHAR(60) NOT NULL,
    Telefono VARCHAR(60) NOT NULL,
    Genero VARCHAR(60) NOT NULL,
    Email VARCHAR(60) NOT NULL,
    FOREIGN KEY (Identificacion) REFERENCES Usuarios(ID_LOGIN)
);


CREATE TABLE Auxiliar{
    ID_AUXILIAR SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

CREATE TABLE Enfermero{
    ID_ENFERMERO SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

CREATE TABLE Familiar{
    ID_FAMILIAR SERIAL NOT NULL PRIMARY KEY,
    parentesco VARCHAR(60) NOT NULL,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

CREATE TABLE Usuarios(
	ID_LOGIN varchar(60) PRIMARY KEY NOT NULL,
	ID_ROL INT NOT NULL,
	Contraseña varchar(60) NOT NULL,
	FOREIGN KEY (ID_ROL) REFERENCES Rol(ID_ROL)
);

CREATE TABLE Medico (
    ID_MEDICO SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    Especialidad VARCHAR(60) NOT NULL,
    Registro VARCHAR(60) NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES Persona(ID_PERSONA)
);

CREATE TABLE Paciente (
    ID_PACIENTE SERIAL NOT NULL PRIMARY KEY, 
    Persona_ID_PERSONA INT NOT NULL,
    Medico_ID_MEDICO INT NOT NULL,
    Familiar_ID_FAMILIAR INT NOT NULL,
    Direccion CHAR(255) NOT NULL,
    Ciudad CHAR(60) NOT NULL,
    Latitud DECIMAL(6,5) NOT NULL,
    Longitud DECIMAL(6,5) NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    FOREIGN KEY (Persona_ID_PERSONA) REFERENCES Persona(ID_PERSONA),     
    FOREIGN KEY (Medico_ID_MEDICO) REFERENCES Medico(ID_MEDICO),
    FOREIGN KEY (Familiar_ID_FAMILIAR) REFERENCES Familiar(ID_FAMILIAR)
);

CREATE TABLE Registro_SV(
    ID_REGISTRO_SV SERIAL NOT NULL PRIMARY KEY, 
    SV_ID_SIGNO_VITAL INT NOT NULL,
    Paciente_ID_PACIENTE INT NOT NULL,
    Medida DECIMAL(6,3) NOT NULL,
    Fecha_Hora DATETIME NOT NULL,
    FOREIGN KEY (SV_ID_SIGNO_VITAL) REFERENCES Signos_vitales(ID_SIGNO_VITAL),
    FOREIGN KEY (Paciente_ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE)
);

CREATE TABLE T_Diagnostico (
    ID_DIAGNOSTICO SERIAL NOT NULL PRIMARY KEY,
    ID_PACIENTE INT NOT NULL,
    ID_MEDICO INT NOT NULL,
    Diagnostico TEXT NOT NULL,
    fecha_hora TIMESTAMPTZ NOT NULL,
    FOREIGN KEY(ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE), 
    FOREIGN KEY (ID_MEDICO) REFERENCES Medico(ID_MEDICO)    
);
    
    
CREATE TABLE T_Sugerencias (
    ID_SUGERENCIAS SERIAL NOT NULL PRIMARY KEY,
    ID_MEDICO INT NOT NULL,
    ID_DIAGNOSTICO BIGINT NOT NULL,
    fecha_hora TIMESTAMPTZ NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY(ID_MEDICO) REFERENCES Medico(ID_MEDICO),
    FOREIGN KEY(ID_DIAGNOSTICO) REFERENCES T_Diagnostico(ID_DIAGNOSTICO)
);

