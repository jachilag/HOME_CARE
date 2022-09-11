INSERT INTO Signos_vitales (Tipo_Signo) VALUES
    ('Oximetria'),
    ('Frec_respiratoria'),
    ('Frec_cardiaca'),
    ('Temperatura'),
    ('Presion_arterial'),
    ('Glicemias');

INSERT INTO Rol (Rol) VALUES 
    ('Médico'),
    ('Auxiliar'),
    ('Paciente'),
    ('Familiar'),
    ('Enfermero'),
    ('Administrador'),
    ('Usuario');

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

INSERT INTO Auxiliar (ID_PERSONA) VALUES -- revisar cual es el id asignado por la tabla persona
    (12),
    (13);

INSERT INTO Enfermero (ID_PERSONA) VALUES 
    (14),
    (15);

INSERT INTO Familiar(parentesco, ID_PERSONA) VALUES
    ('Hermano', 16),
    ('Hermano', 17);

INSERT INTO Especialidad (especialidad) VALUES 
    ('Pediatria'),
    ('Medicina General'),
    ('Dermatologia'),
    ('Cardialogia');

INSERT INTO Medico (ID_PERSONA, ID_ESPECIALIDAD, Registro) VALUES
    (18,1,'hola 1'),
    (19,2,'hola 2');

INSERT INTO Paciente (Persona_ID_PERSONA, Medico_ID_MEDICO, Familiar_ID_FAMILIAR, Direccion, Ciudad, Latitud, Longitud, Fecha_Nacimiento) VALUES 
    (20, 1, 1, 'kr 60 x cl 60', 'Bogota', 4.576, -74.12, '1991-03-01'),
    (21, 2, 2, 'tr 50 x dg 50', 'Manizales', 5.577, -75.12, '2000-01-01');

INSERT INTO Registro_SV (SV_ID_SIGNO_VITAL, Paciente_ID_PACIENTE, Medida, Fecha_Hora) VALUES 
    (1, 3, 1.25, '01-01-2020 12:00:30'),
    (2, 3, 2.25, '01-01-2020 12:10:30'),
    (6, 4, 13.14, '01-01-2020 12:20:30'),
    (3, 3, 3.1415, '01-01-2020 12:30:30'),
    (4, 4, 6.21, '01-01-2020 12:40:30'),
    (5, 4, 0.036, '01-01-2020 12:50:30');

INSERT INTO T_Diagnostico (ID_PACIENTE, ID_MEDICO, Diagnostico, fecha_hora) VALUES 
    (3, 1, 'Pereza', '03-09-2022 16:00:30'),
    (4, 2, 'Hambre', '04-09-2022 16:35:30');    
    
INSERT INTO T_Sugerencias (ID_MEDICO, ID_DIAGNOSTICO, fecha_hora, descripcion) VALUES
    (1, 1, '03-09-2022 18:00:30', 'Trabaje vago'),
    (2, 2, '04-09-2022 19:00:30', 'Duerma 8 horas diarias');
