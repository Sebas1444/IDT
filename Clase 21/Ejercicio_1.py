print("\n\n(1)------------------------------------Leer los tres lados de un triángulo escaleno. Calcular su perímetro------------------------------------")
lado1=0
lado2=0
lado3=0

lado1=int(input("\nIngrese lado A: "))
lado2=int(input("\nIngrese lado B: "))
lado3=int(input("\nIngrese lado C: "))

perimetro=lado1+lado2+lado3

print("El perímetro del triangulo escaleno es: ",perimetro)

print("\n\n(2)------------------------------------Leer un número cualquiera y emitir el siguiente mensaje nulo(si es cero), o positivo o negativo según sea el valor del número------------------------------------")
n=0
n=int(input("\nIngrese un numero: "))

if(n<0):
    print("El numero ingresado es NEGATIVO")
elif (n>0):
    print("El numero ingresado es POSITIVO")
else:
    print("El numero ingresado es NULO")

print("\n\n(2)------------------------------------Leer dos variables N1 y N2. Ver si N1 es positivo, si lo es elevarlo al cuadrado e imprimir el resultado. Y si N1 es 0 ó negativo sumarlo a N2 y entonces elevar al cuadrado la suma para imprimir elresultado------------------------------------")
n1=0
n2=0
n3=0
n1=int(input("\nIngrese un numero: "))
n2=int(input("\nIngrese otro numero: "))

if(n1<=0):
    n3=n1+n2
    n3= n3**2
    print("El numero ingresado es negativo por lo tanto lla raiz cuadrada de la suma de los dos numeros es: ",n3)

else:
    n1= n1**2
    print("El numero ingresado es positivo por lo tanto la raiz cuadrada de dicho numero es: ",n1)

print("\n\n------------------------------------Elaborar un programa que permita leer un solo número e imprima su cubo------------------------------------")
n=0
n=int(input("\nIngrese un numero: "))
n= n*n*n
print ("El cubo del numero es: ",n)

print("\n\n------------------------------------Escriba un programa que lea un número negativo e imprima el número y el positivo del mismo------------------------------------")
n1=0
n2=0
n1=int(input("\nIngrese un número: "))
n2=n1*(-1)
print("El numero negativo en POSITIVO es: ",n2)

print("\n\n------------------------------------Se desea un programa para convertir metros a pies y pulgadas (1 metro = 39.37 pulgadas, 1 pie = 12 pulgadas)------------------------------------")
m=0
pl=0
p=0
m=int(input("Ingrese la cantidad de metros: "))
p=m*3.281
pl=m*39.37
print("La cantidad de Metros es: ",m," ,la cantidad de Pies es: ",p," y las Pulgadas son :",pl)