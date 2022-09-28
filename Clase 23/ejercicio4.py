#1- Hacer un programa que imprima del 10 al 0 en orden
#decreciente.
print("--------------------Ejercicio1--------------------")
def imprimirDecreciente(desde, hasta):
    if(desde>hasta):
        while(desde >hasta):
            print(desde)
            desde=desde-1
            
        else:
            while(desde <hasta):
                print(desde)
                desde=desde+1
imprimirDecreciente(10,0)

#2- Hacer un programa que imprima los números pares
#del 0 al 10.
print("--------------------Ejercicio2--------------------")
def imprimirPares(desde, hasta):
    if(desde>hasta):
        while(desde >hasta):
            print(desde)
            desde=desde-1
        print("hasta")
    else:
         while(desde <hasta):
            desde=desde+1
            if(desde%2==0):
                print(desde," es par.")
imprimirPares(-1,11)
#3- Hacer un programa que imprima la suma de los
#números del 1 al 10
print("--------------------Ejercicio3--------------------")
def sumar(desde,hasta):
    aux=desde
    suma=0
    while(desde<=hasta):
        suma=suma+desde
        desde=desde+1
    print("La suma desde",aux,"hasta",hasta,"es de: ",suma)
sumar(1,10)
#4- Hacer un programa que imprima los números
#impares entre el 10 y el cero en orden decreciente y
#que calcule la suma de esos números impares.
print("--------------------Ejercicio4--------------------")
def imprimirDecreciente(desde, hasta):
    aux=10
    while (aux>=0):
        if (aux%2==1):
            print(aux)
        aux=aux-1
imprimirDecreciente(10,0)
def sumar(desde,hasta):
    aux=desde
    suma=0
    while(desde<=hasta):
        suma=suma+desde
        desde=desde+1
    print("La suma desde el 10 hasta el 0 es de: ",suma)
sumar(1,10)

#5- Hacer un programa que imprima todos los números
#enteros que hay desde la unidad hasta un número
#que introduciremos por teclado.
print("--------------------Ejercicio5--------------------")
contador=0
n=0
n=int(input("Introduce un número: "))
while(contador<n):
    contador=contador+1
    print(contador)

#6- Introducir por teclado tantas frases como se deseen
#y contarlas.
print("--------------------Ejercicio6--------------------")
from cmd import PROMPT
contador=0
n=1
prompt="\nIngrese una frase ";prompt+=" o ingresa 'salir' para salir del programa: "
while (n==1):
    contador=contador+1
    opcion=input(prompt)
    if opcion=='salir':
        break
contador=contador-1
print("el numero de frases son: ",contador)
#7- Hacer un programa que imprima y cuente los
#múltiplos de 3 que hay entre el 0 y el 20.
print("--------------------Ejercicio7--------------------")
def contar(numero):
    multiplos= [ ]
    for i in range(1, numero+1):
        if numero % i==0:
            multiplos.append(i)
    return multiplos
d=contar(20)
print(d)
#8- Ingresar 5 numeros por teclado y al final de los
#mismos, el programa debe emitir los siguientes
#datos: Suma total, Cantidad de numeros impares, y
#un mensaje que indique si existen números
#superiores a 100
print("--------------------Ejercicio8--------------------")

n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese un número: "))
n3=int(input("Ingrese un número: "))
n4=int(input("Ingrese un número: "))
n5=int(input("Ingrese un número: "))

def sumaTotal(x1,x2,x3,x4,x5):
    return x1+x2+x3+x4+x5

def cantImpar(x1,x2,x3,x4,x5):
    cantidad=0
    if(x1%2==1):
        cantidad += 1
    if(x2%2==1):
        cantidad += 1
    if(x3%2==1):
        cantidad += 1
    if(x4%2==1):
        cantidad += 1
    if(x5%2==1):
        cantidad += 1
    return cantidad
def superiorA100(x1,x2,x3,x4,x5):
    if(x1>100):
        print("Existen valores superiores a 100!")
    elif(x3>100):
        print("Existen valores superiores a 100!")
    elif(x4>100):
        print("Existen valores superiores a 100!")
    elif(x5>100):
        print("Existen valores superiores a 100!")
    else:
        print("NO Existen valores superiores a 100!")

print("Suma total: ", sumaTotal(n1,n2,n3,n4,n5))
print("Cantidad impar: ", cantImpar(n1,n2,n3,n4,n5))
superiorA100(n1,n2,n3,n4,n5)