create table agenda(
	apellido varchar(30),
	nombre varchar(20),
	domicilio varchar(30),
	telefono varchar(11)
);
insert into agenda(apellido,nombre,domicilio,telefono)
	values('Alvarez','Alberto','Colon 123','4234567'),('Juarez','Juan','Avellaneda 135','4458787'),('Lopez','Maria','Urquiza 333','4545454'),('Lopez','Jose','Urquiza 333','4545454'),('Salas','Susana','Gral. Paz 1234','4123456');

	
create table cursos(
	id int,
	descripcion varchar(30)
);
insert into cursos values (1, 'Desarrollo Web'),(2, 'Introduccion a la programacion'),
(3, 'Marketing'),(4,'Diseño Grafico');

select * from cursos c;

create table inscripciones(
	id int auto_increment,
	idcurso int,
	idpersona int,
	primary key(id)

);

select * from agenda;

alter table agenda add column id int;

alter table agenda add primary key (id);

describe agenda;

insert into inscripciones (idcurso, idpersona) values (1,1),(1,2),(3,1),(4,3),(3,4);

select * from inscripciones i ;

select * from agenda a 
inner join inscripciones i;

select a.id as 'id Persona', i.id as 'id Inscripcion' from agenda a 
inner join inscripciones i;

select a.nombre, a.apellido, i.idcurso, c.descripcion  from agenda a 
inner join inscripciones i on i.idpersona = a.id
inner join cursos c on i.idcurso = c.id 
;

select date(NOW());

alter table agenda add column FechaNacimiento date;

select *	from agenda a ;

update agenda a set	a.FechaNacimiento = '2000-12-14' where id between 2 and 5;

select * from agenda a where id between 2 and 5;

update agenda a set	a.FechaNacimiento = '1991-06-04' where id =5;

select a.nombre, a.apellido, a.FechaNacimiento,(year(now()) - year (a.FechaNacimiento)) as edad 
if()
from agenda a;




