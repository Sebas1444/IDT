print("--------------------Ejercicio 1 --------------------")
for i in range(1,10):
        print("El cuadrado de", i ,"es",i**2)
print("\n")
print("\n")

print("--------------------Ejercicio 2 --------------------")
numero = int(input("Ingrese el nro:"))
suma = 0
if (numero % 2 == 1):
    numero +=1
   
for i in range(4):
     suma = suma + numero
     numero +=2
print("La suma de los primeros nros pares es: ",suma)
print("\n")
print("\n")

print("--------------------Ejercicio 3 --------------------")
cantidad =int(input("Ingrese la cantidad de espacios en la lista "))
suma = 0
lista = []

for i in range(cantidad):
    numero = int(input("Ingrese un nro para la posicion"+ str(i) + ":"))
    lista.append(numero)
    suma +=  lista[i]

promedio = suma / cantidad
print("La suma de los numero de la lista es:  ",suma)
print("El promedio de los N numero de la lista es : ",promedio)
print("\n")
print("\n")

print("--------------------Ejercicio 4 --------------------")
cantidad = int(input("Ingrese cantidad de numeros:"))
suma = 0
contador = 0
lista = []

for i in range(cantidad):
    numero = int(input("Ingrese un nro para la posicion"+str(i)+":"))
    lista.append(numero)

    if lista[i] != 0:
        suma = suma + lista[i]
        contador +=1
promedio = suma / cantidad
print("El promedio de los nros diferentes a cero es: ", int(promedio))
print("\n")
print("\n")

print("--------------------Ejercicio 5 --------------------")
cantidad = int(input("Ingrese el numero de espacios en la lista que desea: "))
suma = 0 
contador = 0
lista = []
promedio = 0

for i in range(cantidad):
    numero=int(input("Ingrese un numero para la posicion"+str(i)+":"))
    lista.append(numero)
    if lista[i] % 2 ==1:
        suma += lista[i]
        contador += 1
promedio = suma / contador
print("El promedio de los numeros impares es: ",int(promedio))