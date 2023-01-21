<?php
$cadena1 = 1000;
$cadena2 = '1000';
if ($cadena1 == $cadena2) {
echo 'Según == las dos cadenas son iguales';
}
else {
echo 'Según == las dos cadenas NO son iguales';
}
echo '<br>';
if ($cadena1 === $cadena2) {
echo 'Segun === las dos cadenas son iguales';
}
else {
echo 'Segun === las dos cadenas NO son iguales';
}
echo '<br>';
if (strcmp($cadena1, $cadena2) == 0) {
echo 'Segun strcmp las dos cadenas son iguales';
}
else {
echo 'Segun strcmp las dos cadenas NO son iguales';
}
$cadena='640 Kb deberian ser suficientes para cualquiera. Bill Gates';
echo '<p>'.str_pad($cadena,100,'*').'</p>';
echo '<p>'.str_pad($cadena,148,'cool!').'</p>';
echo '<p>'.str_pad($cadena,2,'a').'</p>';
echo '<p>'.str_pad($cadena,100,'*',STR_PAD_LEFT).'</p>';
echo '<p>'.str_pad($cadena,100,'@',STR_PAD_BOTH).'</p>';
?>
