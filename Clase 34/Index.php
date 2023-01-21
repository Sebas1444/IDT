<html>

<head>
    <meta charset=UTF-8">
    <title></title>
</head>

<body>
    Esta es una pagina super simple
    <?php
echo "Me aparecerá esta línea?";
echo "<br><h1><font color='FF0000'>Texto grande y
rojo</font></h1>";
//este comentario no se verá en la página
echo "Esta línea se leerá<br>"; //Esto no se leerá
/*Este es un comentario de múltiples líneas y no
se acabará hasta
que indiquemos su final así */
#Esta es otra forma de agregar un comentario
# Esta línea obviamente tampoco se leerá
echo ("Aquí va el cuarto texto visible");
/*cuidado con anidar
comentarios como estos
ya que llevan a una mala
interpretación del código*/
?>
</body>

</html>