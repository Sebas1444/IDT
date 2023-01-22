<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
//# Conectamos con MySQL
require_once('../../../../php/conexion.php');
$nombre_usuario = $_REQUEST['nombre_usuario'];
$login_usuario = $_REQUEST['login_usuario'];
$pass_usuario = $_REQUEST['pass_usuario'];
$sql="insert into usuarios(nombre_usuario,login_usuario,
pass_usuario) VALUES ('".$nombre_usuario."','".$login_usuario."',
'".$pass_usuario."')";
$ret=$mysqli->query($sql);
$res="Mensaje No enviado";
if($ret==1){
$res="Usuario agregado satisfactoriamente";
}
$mysqli->close();
echo($res);
?>
</body>
</html>