print("\n\n\n-------------------------------------Hallar el promedio de tres números enterosingresados por teclado.-------------------------------------")
n1=0;n2=0; n3=0; promedio=0
n1=int(input("Por favor ingrese el primer valor: "))
n2=int(input("Por favor ingrese el segundo valor: "))
n3=int(input("Por favor ingrese el tercer valor: "))
promedio=(n1+n2+n3)/3

print("El promedio de los tres numero es de: ",promedio)

print("\n\n\n-------------------------------------Hallar el área y perímetro de un cuadrado.-------------------------------------")
lado=0
lado=int(input("Ingrese unos de los lados del cuadrado: "))
perimetro=lado*4
area=lado **2

print("El area del cuadrado es de: ",area,",y su perimtro es: ",perimetro)

print("\n\n\n-------------------------------------Un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes, si el banco paga a 2% de interés mensual.-------------------------------------")
cap=0
interes=0
cap=int(input("Ingrese el dinero a ser invertido: "))
interes=(cap*0.2*1)
total=cap+interes
print("La ganancia de la inversión es de: ",total)

print("\n\n\n--------------------------------------Programa que se lea un número entero por teclado y se indique si el numero introducido es par o impar.-------------------------------------")
n=int(input("Ingrese un número: "))
if n % 2 == 0:
    print("El numero",n," es par")
else:
    print("El número es impar")

print("\n\n\n--------------------------------------Declara 2 variables numéricas (con el valor que desees), he indica cual es mayor de los dos. Si soniguales indicarlo también. Vas cambiando los valores para comprobar que funciona.-------------------------------------")
n1=0; n2=0
n1=int(input("Favor ingrese el primer numero: "))
n2=int(input("Favor ingrese el segundo numero: "))

if n1>n2:
    print("El primer numero: ",n1,", es mayor que:",n2)
elif n1<n2:
    print("El segundo numero:",n2," es mayor que",n1)
else:
    print("El primer numero",n1," es igual al segundo numero",n2)

print("\n\n\n--------------------------------------Lee un número por teclado e indica si es divisible por 3. Si no lo es, también debemos indicarlo-------------------------------------")
n=0

n=int(input("Ingrese un numero: "))
if n%3!=0:
    print("El numero ",n,"no es divisible por 3")
else:
    print("El numero ingresado es divisible por 3")

