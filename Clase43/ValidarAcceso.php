<?php
require_once('conexion.php');
$login_usuario = $_POST['login_usuario'];
$password_usuario = $_POST['password_usuario'];
$sql="select * from usuarios where login_usuario='"
.$login_usuario."' and pass_usuario='".$password_usuario."'";
$ret=$mysqli->query($sql);
session_start();
$_SESSION['acceso']="false";
if($ret->num_rows==1){
$_SESSION['acceso']="true";
}
$pregunta = new stdClass();
$pregunta->acceso = $_SESSION['acceso'];
$json = json_encode($pregunta);
$mysqli->close();
echo($json);
?>