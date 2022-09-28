#1- En una tienda se ha establecido la siguiente oferta: por
#compras menores a 100.000 se hace un descuento de 8%, pero
#para compras a partir de 100.000 el descuento es de 10%. Se
#pide ingresar la cantidad y el precio del producto que se compra
#y determinar cuánto se descontará y cuanto se cobrará.

print("-------------Ejercicio 1-------------")
cant=0; precio=0;pc=100000;a=0
cant=int(input("Ingrese la cantidad de producto que deseas comprar: "))
precio=int(input("Ingrese el precio del producto que deseas comprar: "))

total=cant*precio
if total<pc:
    a=(total*92/100)
    print("El descuento obtenido por el valor de la compra es del 8%, el precio a pagar final es de :",a)
else:
    a=(total*90/100)
    print("El descuento obtenido por el valor de la compra es del 10%, el precio a pagar final es de :",a)

#2- Una empresa quiere hacer una compra de varias piezas de la
#misma clase en una fábrica de refacciones. La empresa
#dependiendo del monto total de la compra decidirá qué hacer
#para pagar al fabricante.
#Si el monto total de la compra excede de 500.000 la empresa
#tendrá la capacidad de invertir de su propio dinero un 55% del
#monto de la compra, pedir prestado al banco un 30% y el resto lo
#pagará solicitando un crédito al fabricante.
#Si el monto total de la compra NO excede de 500.000 la empresa
#tendrá capacidad de invertir de su propio dinero un 70% y el
#restante 30% lo pagará solicitando crédito al fabricante.
#El fabricante cobra por concepto de intereses un 20% sobre la
#cantidad que se le pague a crédito.

print("\n\n\n-------------Ejercicio 2-------------")
cant=0; precio=0;pc=500000;a=0;total=0;inver55=0;inver70=0;prestamo=0
cant=int(input("Ingrese la cantidad de producto que deseas comprar: "))
precio=int(input("Ingrese el precio del producto que deseas comprar: "))
total=cant*precio
inver55=total*55/100
inver70=total*70/100
prestamo=total*30/100
saldo55=total-(inver55+prestamo)
saldo70=total-inver70
interes55=saldo55*120/100
interes70=saldo70*120/100
if total>pc:
        print("El monto total de compra es de: ",total,", el dinero a invertir es del 55%: ",inver55,", se realizará un prestamo del banco por el 30% del valor de la compra: ",prestamo," y el resto (",saldo55,")se pagará solicitando un credito al fabricante.")
        print("El fabricante cobrará un interés del 20% sobre la cantidad del pago a credito: ",interes55)
else:
    print("El monto total de compra es de: ",total,", el dinero a invertir es del 70%: ",inver70," y el restante(",saldo70,")se pagará solicitando un credito al fabricante.")
    print("El fabricante cobrará un interés del 20% sobre la cantidad del pago a credito: ",interes70)

#3- Un vendedor recibe un sueldo base más un 10% extra por
#comisión de sus ventas, el vendedor desea saber cuánto dinero
#obtendrá por concepto de comisiones por las tres ventas que
#realiza en el mes y el total que recibirá en el mes tomando en
#cuenta su sueldo base más comisiones.

print("\n\n\n-------------Ejercicio 3-------------")
sueldo=0;comicion=0
sueldo=int(input("Ingrese su sueldo: "))
venta=int(input("Ingrese la cantidad de venta que realizó: "))
sueldo10=sueldo*10/100
Sueldof=sueldo10*venta
total=sueldo+Sueldof
print("El sueldo más la comición es de: ",total)
#4- Una tienda ofrece un descuento del 15% sobre el total de la
#compra, y un cliente desea saber cuánto deberá pagar finalmente
#sobre su compra.
print("\n\n\n-------------Ejercicio 4-------------")
print("\n\n\n-------------Bienvenido a la tienda de los descuentos-------------")
porductos=0;cantidad=0;precio=0
cantidad=int(input("Ingrese el precio del producto que desea comprar: "))
productos=int(input("Ingrese la cantidad de productos que desea comprar: "))
print("\n\nLe informamos que el día de hoy tenemos descuento del 15% en todos los productos en promocion")
precio=(productos*cantidad)*85/100
print("Por ende el precio final es de: ",precio)

#Calcular el nuevo salario de un obrero si obtuvo un incremento
#del 25% sobre su salario anterior.
print("\n\n\n-------------Ejercicio 5-------------")
salariov=0;salarion=0
salariov=int(input("Ingrese el valor de su salario anterior al aumento: "))
salarion=(salariov*1.25)

print("El salario nuevo a persivir es de: ",salarion)

#Leer dos números, si son iguales que se multipliquen, si el
#primero es mayor que el segundo que se resten y sino que se
#sumen.
print("\n\n\n-------------Ejercicio 6-------------")
n1=0;n2=0;n3=0
n1=int(input("Por favor ingrese un numero: "))
n2=int(input("Por favor ingrese otro numero: "))

if n1==n2:
    n3=n1*n2
    print("Los numeros ingresados son iguales, la multiplicación de los mismos son: ",n3)
elif n1>n2:
    n3=n1-n2
    print("El primero es mayor que el segundo por lo tanto la resta del primero numero con el segundo es: ",n3)
else :
    n3=n1+n2
    print("El resultado de la suma de los dos numero son: ",n3)

    
#El IPS quiere clasificar a las personas que se jubilarán en el año
#2017. Existen tres tipos de jubilaciones, por edad, por antigüedad
#joven y por antiguedad adulta. 
# 
# Las personas para la jubilación por edad deben tener 60 años o más y una antigüedad en su empleo
#de menos de 25 años.
#Las personas para la jubilación por antigüedad joven deben tener
#menos de 60 años y una antigüedad en su empleo de 25 años o
#más.
#Las personas para antigüedad adulta deben tener 60 años o más
#y una antigüedad en su empleo de 25 años o más.

print("\n\n\n-------------Ejercicio 7-------------")
antiguedad=0;edad=0;
print("\n\n\n-------------Clasificación de Jubilados-------------")
edad=int(input("Ingrese su edad: "))
antiguedad=int(input("Ingrese su antiguedad laboral: "))
if edad<60:
    print("Tu Jubilación es por antigüedad joven, es decir tu la edad requerida es menos de 60 años y una antiguedad laboral de 25 años.")
else:
    if antiguedad<25:
            print("La Jubilacion es por edad, es decir la edad requerida es de 60 años o mas y una antiguedad en su empleo de menos 25 años.")
    else: 
            print("La Jubilación es por antiguedad adulta, es decir la edad requerida es de mas de 60 años y la antiguedad laboral 25 años o más.")

#En una tienda se efectúa una promoción en la cual se hace un
#descuento sobre el valor de la cuenta total, según el color de la
#bolilla que el cliente saque al pagar en caja. Si la bolilla es de
#color blanco no se hará descuento alguno, si es verde se le hará
#un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si
#es roja un 100%. Determinar la cantidad final que el cliente
#deberá pagar por su compra. Se sabe que sólo hay bolillas de los
#colores mencionados.

print("\n\n\n-------------Ejercicio 8-------------")
import random
precio=0;total=0
bolitas = ['Blanca','Verde','Amarilla','Azul','Roja']
precio = int(input("Ingrese el precio de la compra total: "))
r = random.choice(bolitas)
print('Salio la bolilla %s' %r)
if r == 'Blanca':
	print("No se aplicó ningun descuento, el total a pagar es",precio)

elif r == 'Verde':
	totGeneral = precio-(precio*0.10)
	print('Total a pagar: %d' %totGeneral)

elif r == 'Amarilla':
	totGeneral = precio-(precio*0.25)
	print('Total a pagar: %d' %totGeneral)
 
elif r == 'Azul':
	totGeneral = precio-(precio*0.50)
	print('Total a pagar: %d' %totGeneral)

else:
	totGeneral = precio-(precio*1)
	print('Total a pagar: %d' %totGeneral)


#Ingresar dos valores en las variables “maximo” y “minimo” y
#luego ingresar un valor en la variable “temperatura”. Imprime un
#mensaje si el valor de temperatura no está dentro del rango de
#marcado por minimo y maximo

print("\n\n\n-------------Ejercicio 9-------------")
maximo=float(input("Introduce un valor de maximo: "))
minimo=float(input("Introduce un valor de minimo: "))
temperatura=float(input("Introduce un valor para la temperatura: "))
if(temperatura>=minimo and temperatura<=maximo):
    print("Estas dentro del rango introducido")
else:
    print("Está fuera del rango introducido")

