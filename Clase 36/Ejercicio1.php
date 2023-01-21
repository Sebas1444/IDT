<?php
$cad = "cadena"; //Prueba a cambiar el texto cadena por otro
$n = strlen($cad);
echo "La longitud de la cadena es: ".$n."<br />";
$sub1 = substr($cad, 2);
$sub2 = substr($cad, 2, 2);
echo "La subcadena número uno es la siguiente: ".$sub1."<br />";
echo "La subcadena número dos es la siguiente: ".$sub2."<br />";
$cad = "Si le das a alguien un programa, lo frustrarás un día. Si le enseñas
a programar, lo frustrarás toda la vida.";
$sub1 = substr($cad, 0); //La cadena completa
$sub2 = substr($cad, 0, 10); //La subcadena Si le das
$sub3 = substr($cad, 8, 1); //La subcadena s
$sub4 = substr($cad, 9); //La subcadena a alguien un programa, lo frustrarás
//un día. Si le enseñas a programar, lo frustrarás toda la vida
echo "La subcadena número uno es la siguiente: ".$sub1." <br />";
echo "La subcadena número dos es la siguiente: ".$sub2." <br />";
echo "La subcadena número tres es la siguiente: ".$sub3." <br />";
echo "La subcadena número cuatro es la siguiente: ".$sub4." <br />";
$cad1 = "concatenando";
$cad2 = "cadenas";
$cadt = $cad1 . $cad2;
echo "La cadena número uno concatenada con la cadena número 2 es: "
.$cadt."<br/>";
// Ahora concatenaremos la cadena ejemplo con la concatenación de $cad2 y
// $cad1
echo "Ejemplo: ".$cad2.$cad1;
?>