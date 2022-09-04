CREATE SCHEMA BD_HOME_CARE;
USE BD_HOME_CARE;

CREATE TABLE Signos_vitales(
    ID_SIGNO_VITAL SERIAL NOT NULL PRIMARY KEY, 
    Tipo_Signo CHAR(60) INT NOT NULL
);

INSERT INTO Signos_vitales (Tipo_Signo) VALUES
    ('Oximetria'),
    ('Frec_respiratoria'),
    ('Frec_cardiaca'),
    ('Temperatura'),
    ('Presion_arterial'),
    ('Glicemias');

CREATE TABLE Rol(
	ID_ROL INT NOT NULL,
	Rol varchar(60) NOT NULL
);

INSERT INTO Rol (Rol) VALUES 
    ('Médico'),
    ('Auxiliar'),
    ('Paciente'),
    ('Familiar'),
    ('Enfermero'),
    ('Administrador');

CREATE TABLE Usuarios(
	ID_LOGIN varchar(60) PRIMARY KEY NOT NULL,
	ID_ROL INT NOT NULL,
	Contraseña varchar(60) NOT NULL,
	FOREIGN KEY (ID_ROL) REFERENCES Rol(ID_ROL)
);

INSERT INTO Usuarios (ID_LOGIN, ID_ROL, Contraseña) VALUES 
    ('123', 1, 'hola123456'),
    ('456', 1, 'hola123456'),
    ('789', 2, 'hola123456'),
    ('147', 2, 'hola123456'),
    ('258', 3, 'hola123456'),
    ('369', 3, 'hola123456'),
    ('321', 4, 'hola123456'),
    ('654', 4, 'hola123456'),
    ('987', 5, 'hola123456'),
    ('741', 5, 'hola123456'),
    ('000', 6, 'hola123456');

CREATE TABLE Persona(
    ID_PERSONA SERIAL NOT NULL PRIMARY KEY,
    Identificacion VARCHAR(60) NOT NULL,
    Nombre VARCHAR(60) NOT NULL,
    Apellido  VARCHAR(60) NOT NULL,
    Telefono VARCHAR(60) NOT NULL,
    Genero VARCHAR(60) NOT NULL,
    Email VARCHAR(60) NOT NULL,
    FOREIGN KEY (Identificacion) REFERENCES Usuarios(ID_LOGIN)
);

INSERT INTO Persona(Identificacion, Nombre, Apellido, Telefono, Genero, Email) VALUES 
    ('123', 'Jessica', 'Guio', '320123', 'Femenino', 'jessica@gmail.com'),
    ('456', 'Jefferson', 'Yagamma', '320456', 'Masculino', 'jefferson@gmail.com'),
    ('789', 'Alejandro', 'Vargas', '320789', 'Masculino', 'alejandro@gmail.com'),
    ('147', 'Jeisson', 'Carreno', '320147', 'Masculino', 'jeisson@gmail.com'),
    ('258', 'Jonathan', 'Chila', '320258', 'Masculino', 'jachilag@gmail.com'),
    ('369', 'Johann', 'Hernandez', '320369', 'Masculino', 'Johann@gmail.com'),
    ('321', 'Jesus', 'Palacio', '320321', 'Masculino', 'Jesus@gmail.com'),
    ('654', 'Jenny', 'Toro', '320654', 'Femenino', 'Jenny@gmail.com'),
    ('987', 'Montserrat', 'Sanchez', 'Femenino', '320987', 'Montserrat@gmail.com'),
    ('741', 'Johan', 'Forero', '320741', 'Masculino', 'Johan@gmail.com'),
    ('000', 'Administrador', 'administrador', '320000', 'Masculino', 'Administrador@gmail.com');

CREATE TABLE Auxiliar{
    ID_AUXILIAR SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

INSERT INTO Auxiliar (ID_PERSONA) VALUES -- revisar cual es el id asignado por la tabla persona
    (12),
    (13);

CREATE TABLE Enfermero{
    ID_ENFERMERO SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

INSERT INTO Enfermero (ID_PERSONA) VALUES 
    (14),
    (15);

CREATE TABLE Familiar{
    ID_FAMILIAR SERIAL NOT NULL PRIMARY KEY,
    parentesco VARCHAR(60) NOT NULL,
    ID_PERSONA INT NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES persona(ID_PERSONA)
};

INSERT INTO Familiar(parentesco, ID_PERSONA) VALUES
    ('Hermano', 16),
    ('Hermano', 17);

CREATE TABLE Especialidad (
    ID_ESPECIALIDAD SERIAL NOT NULL PRIMARY KEY,
    especialidad varchar(60) NOT NULL
);

INSERT INTO Especialidad (especialidad) VALUES 
    ('Pediatria'),
    ('Medicina General'),
    ('Dermatologia'),
    ('Cardialogia');

CREATE TABLE Medico (
    ID_MEDICO SERIAL NOT NULL PRIMARY KEY,
    ID_PERSONA INT NOT NULL,
    ID_ESPECIALIDAD INT NOT NULL,
    Registro VARCHAR(60) NOT NULL,
    FOREIGN KEY (ID_PERSONA) REFERENCES Persona(ID_PERSONA)
    FOREIGN KEY (ID_ESPECIALIDAD) REFERENCES Especialidad(ID_ESPECIALIDAD)
);

INSERT INTO Medico (ID_PERSONA, ID_ESPECIALIDAD, Registro) VALUES
    (18,1,'hola 1'),
    (19,2,'hola 2');

CREATE TABLE Paciente (
    ID_PACIENTE SERIAL NOT NULL PRIMARY KEY, 
    Persona_ID_PERSONA INT NOT NULL,
    Medico_ID_MEDICO INT NOT NULL,
    Familiar_ID_FAMILIAR INT NOT NULL,
    Direccion CHAR(255) NOT NULL,
    Ciudad CHAR(60) NOT NULL,
    Latitud DECIMAL(11,8) NOT NULL,
    Longitud DECIMAL(11,8) NOT NULL,
    Fecha_Nacimiento DATE NOT NULL,
    FOREIGN KEY (Persona_ID_PERSONA) REFERENCES Persona(ID_PERSONA),     
    FOREIGN KEY (Medico_ID_MEDICO) REFERENCES Medico(ID_MEDICO),
    FOREIGN KEY (Familiar_ID_FAMILIAR) REFERENCES Familiar(ID_FAMILIAR)
);

INSERT INTO Paciente (Persona_ID_PERSONA, Medico_ID_MEDICO, Familiar_ID_FAMILIAR, Direccion, Ciudad, Latitud, Longitud, Fecha_Nacimiento) VALUES 
    (20, 1, 1, 'kr 60 x cl 60', 'Bogota', 4.576, -74.12, '01-03-1991'),
    (21, 2, 2, 'tr 50 x dg 50', 'Manizales', 5.577, -75.12, '01-01-2000');

CREATE TABLE Registro_SV(
    ID_REGISTRO_SV SERIAL NOT NULL PRIMARY KEY, 
    SV_ID_SIGNO_VITAL INT NOT NULL,
    Paciente_ID_PACIENTE INT NOT NULL,
    Medida DECIMAL(6,3) NOT NULL,
    Fecha_Hora TIMESTAMPTZ NOT NULL,
    FOREIGN KEY (SV_ID_SIGNO_VITAL) REFERENCES Signos_vitales(ID_SIGNO_VITAL),
    FOREIGN KEY (Paciente_ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE)
);

INSERT INTO Registro_SV (SV_ID_SIGNO_VITAL, Paciente_ID_PACIENTE, Medida, Fecha_Hora) VALUES 
    (1, 3, 1.25, '01-01-2020 12:00:30'),
    (2, 3, 2.25, '01-01-2020 12:10:30'),
    (6, 4, 13.14, '01-01-2020 12:20:30'),
    (3, 3, 3.1415, '01-01-2020 12:30:30'),
    (4, 4, 6.21, '01-01-2020 12:40:30'),
    (5, 4, 0.036, '01-01-2020 12:50:30');

CREATE TABLE T_Diagnostico (
    ID_DIAGNOSTICO SERIAL NOT NULL PRIMARY KEY,
    ID_PACIENTE INT NOT NULL,
    ID_MEDICO INT NOT NULL,
    Diagnostico TEXT NOT NULL,
    fecha_hora TIMESTAMPTZ NOT NULL,
    FOREIGN KEY(ID_PACIENTE) REFERENCES Paciente(ID_PACIENTE), 
    FOREIGN KEY (ID_MEDICO) REFERENCES Medico(ID_MEDICO)    
);

INSERT INTO T_Diagnostico (ID_PACIENTE, ID_MEDICO, Diagnostico, fecha_hora) VALUES 
    (3, 1, 'Pereza', '03-09-2022 16:00:30'),
    (4, 2, 'Hambre', '04-09-2022 16:35:30');    
    
CREATE TABLE T_Sugerencias (
    ID_SUGERENCIAS SERIAL NOT NULL PRIMARY KEY,
    ID_MEDICO INT NOT NULL,
    ID_DIAGNOSTICO BIGINT NOT NULL,
    fecha_hora TIMESTAMPTZ NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY(ID_MEDICO) REFERENCES Medico(ID_MEDICO),
    FOREIGN KEY(ID_DIAGNOSTICO) REFERENCES T_Diagnostico(ID_DIAGNOSTICO)
);

INSERT INTO T_Sugerencias (ID_MEDICO, ID_DIAGNOSTICO, fecha_hora, descripcion) VALUES
    (1, 1, '03-09-2022 18:00:30', 'Trabaje vago'),
    (2, 2, '04-09-2022 19:00:30', 'Duerma 8 horas diarias');


