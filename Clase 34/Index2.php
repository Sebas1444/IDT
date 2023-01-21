<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title></title>
</head>

<body>
    <?php
#Defino la variable pepe como cadena vacía
$pepe="";
#Defino las variables $Pepe y $Pepa (ojo con mayusculas iniciales)
$Pepe="Me llamo Pepe y soy serio y formal";
$Pepa="Me llamo Pepa y también soy seria y formal";
?>
    <center><b>Vamos a ver el contenido de las variables</b></center>
    <?php
echo "<br>El valor de la variable pepe es: ".$pepe;
echo "<br>No se ha mostrado nada porque la variable pepe esta vacía";
echo "<br>El valor de la variable Pepe es: ".$Pepe;
?>
</body>

</html>