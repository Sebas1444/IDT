//1- Crearemos una tabla llamada "agenda". Debe tener los siguientes campos:
apellido (cadena de 30), nombre (cadena de 20), domicilio (cadena de 30) y
telefono (cadena de 11);
//2- Ingrese los siguientes registros:
insert into agenda (apellido, nombre, domicilio, telefono)
values ('Moreno','Alberto','Colon 123','4234567');
insert into agenda (apellido,nombre, domicilio, telefono)
values ('Torres','Juan','Avellaneda 135','4458787');
//3- Seleccione todos los registros de la tabla:
select * from agenda;
//4- Elimine la tabla "agenda"
drop table agenda
//5- Intente eliminar la tabla nuevamente (aparece un mensaje de error)
Ejercicio 2 Modificar Registros (update)
Trabaje con la tabla "agenda" que almacena los datos de sus amigos.
1- Cree la tabla como en el ejercicio 1
2- Ingrese los siguientes registros:
'Acosta','Alberto','Colon 123','4234567'
'Juarez','Juan','Avellaneda 135','4458787'
'Lopez','Maria','Urquiza 333','4545454'
'Lopez','Jose','Urquiza 333','4545454'
'Suarez','Susana','Gral. Paz 1234','4123456'
//3- Modifique el registro cuyo nombre sea "Juan" por "Juan Jose" (1 registro
afectado)
update agenda set nombre='Juan Jose' where nombre='Juan';
//4- Actualice los registros cuyo número telefónico sea igual a "4545454" por
"4445566" (2 registros afectados)
update agenda set telefono='4445566' where telefono='4545454';
//5- Actualice los registros que tengan en el campo "nombre" el valor "Juan" por
"Juan Jose" (ningún registro afectado porque ninguno cumple con la condición del
"where")
update agenda set nombre='Juan Jose' where nombre='Juan';
//6 - Luego de cada actualización ejecute un select que muestre todos los registros
de la tabla.
Ejercicio 3 Eliminar Registros (delete)
Trabaje con la tabla "agenda" que registra la información referente a sus amigos.
1- Cree la tabla con los siguientes campos: apellido (cadena de 30), nombre
(cadena de 20), domicilio (cadena de 30) y telefono (cadena de 11) como en el
ejercicio 1
//2- Ingrese los siguientes registros (insert into):
Alvarez,Alberto,Colon 123,4234567,
Juarez,Juan,Avellaneda 135,4458787,
Lopez,Maria,Urquiza 333,4545454,
Lopez,Jose,Urquiza 333,4545454,
Salas,Susana,Gral. Paz 1234,4123456.
//3- Elimine el registro cuyo nombre sea "Juan" (1 registro afectado)
delete from agenda where nombre='Juan';
//4- Elimine los registros cuyo número telefónico sea igual a "4545454" (2 registros
afectados)
delete from agenda where telefono='4545454';
//5- Muestre la tabla.
select * from agenda;
//6- Elimine todos los registros (2 registros afectados)
delete from agenda;
//7- Muestre la tabla.
select * from agenda;
//Ejercicio 4 Seleccionar Registros (select)
Trabaje con la tabla "agenda" en la que registra los datos de sus amigos.
//1- Cree la tabla, con los siguientes campos: apellido (cadena de 30), nombre
(cadena de 20), domicilio (cadena de 30) y telefono (cadena de 11).
//2- Ingrese los siguientes registros:
Acosta, Ana, Colon 123, 4234567;
Bustamante, Betina, Avellaneda 135, 4458787;
Lopez, Hector, Salta 545, 4887788;
Lopez, Luis, Urquiza 333, 4545454;
Lopez, Marisa, Urquiza 333, 4545454.
//3- Seleccione todos los registros de la tabla
//4- Seleccione el registro cuyo nombre sea "Marisa" (1 registro)
select * from agenda where nombre='Marisa';
//5- Seleccione los nombres y domicilios de quienes tengan apellido igual a "Lopez"
(3 registros)
select nombre,domicilio from agenda where apellido='Lopez';
//6- Muestre el nombre de quienes tengan el teléfono "4545454" (2 registros)
select nombre from agenda where telefono='4545454';