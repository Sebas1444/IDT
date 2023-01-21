<?php
// Iremos leyendo línea a línea del fichero.txt hasta llegar al fin (feof($fp))
// fichero.txt tienen que estar en la misma carpeta que el fichero php
// fichero.txt es un archivo de texto normal creado con notepad, por ejemplo.
//r Abre el archivo sólo para lectura. La lectura comienza al inicio del archivo
//r+ Abre el archivo para lectura y escritura. La lectura o escritura comienza
//al inicio del archivo.
//w Abre el archivo sólo para escritura. La escritura comienza al inicio del
//archivo, y elimina el contenido previo. Si el archivo no existe, intenta
//crearlo.
//w+ Abre el archivo para escritura y lectura. La lectura o escritura comienza
//al inicio del archivo, y elimina el contenido previo. Si el archivo no existe,
// intenta crearlo.
//a Abre el archivo para sólo escritura. La escritura comenzará al final del
//archivo, sin afectar al contenido previo. Si el fichero no existe se intenta
// crear.
//a+ Abre el archivo para lectura y escritura. La lectura o escritura comenzará
//al final del fichero, sin afectar al contenido previo. Si el fichero no existe
// se intenta crear.
$fp = fopen("fichero.txt", "r+");
while (!feof($fp)) {
$linea = fgets($fp);
echo $linea . "<br>";
}
fwrite($fp, "Prueba de escritura" . PHP_EOL);
fclose($fp);
?>