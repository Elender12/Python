'''1. Escriba un programa que calcule hel área de un triángulo (base x altura/2),
pidiendo los datos base y altura al usuario.

print("Introduce el la base del triángulo: ")
base= int(input())
print("Introduce la altura del triángulo: ")
altura=int(input())
def areaTriangulo(base, altura):
    resultado = (base * altura)/2
    print("El área del triángulo es la siguiente ",resultado)
areaTriangulo(base,altura)
    
#puedo convertir el número cuando leo por teclado o cuando se lo paso como parámetro
'''

'''2. Escriba un programa que determine
 si un número leído desde teclado es positivo, negativo, o cero.
def tipoNumero(num):
    if num >= 1:
        print("el número es positivo")
    elif num < 0:
        print("el número es negativo")
    elif num == 0:
        print("has introducido 0")
    else:
        print("has introducido otra cosa")
#puedo asignar directamente lo que leo por pantalla a una variable
num = int(input("Introduce un número: "))
tipoNumero(num)
'''
'''3.Escriba un programa que lea dos números desde teclado y si el primero es mayor que el segundo
intercambie sus valores y los muestre ordenados por pantalla
(después de haber intercambiado el valor de las variables correspondientes).
num1= int(input("Introduzca el primer número: "))
num2= int(input("Introduzca el segundo número: "))
def intercambioNum(num1,num2):
    if num1>num2:
        print(num1," es el mayor")
        aux=num1
        num1=num2
        num2=aux
        print("El primer número vale ahora: ",num1," y el segundo vale ",num2)
        
    elif num2>num1:
        print(num2," es el mayor")
    else:
        print("Los números son iguales")
intercambioNum(num1, num2)
'''
'''4. Escriba un programa que pregunte la edad al usuario, la fecha actual,
y si ha cumplido años en el año actual o no,
y en base a esa información calcule su año de nacimiento.
anioActual= int(input("¿En qué año estamos? "))
edad= int(input("¿Cuál es tu edad: "))
res = input("¿Has cumplido años? s/n ")
var= True
if res=="s":
    var= True
elif res=="n":
    var= False
def calcEdad(edad, anioActual,var):
    anNac= anioActual-edad
    if var==False:
        print("Tu año de nacimiento es ",anNac," pero no has cumplido años")
    else:
        print("Tu año de nacimiento es ",anNac)
calcEdad(edad, anioActual,var)
'''

'''5. Escriba un programa que pregunte la edad al usuario, la fecha actual,
y en qué día y mes es su cumpleaños,
y en base a esa información calcule su año de nacimiento.
'''

'''6. Escriba un programa que calcule la cantidad total de segundos a partir de horas,
minutos y segundos pedidos al usuario.

horas = float(input("Introduzca la cantidad de horas: "))
minutos= int(input("introduzca la cantidad de minutos: "))
segundos= int(input("introduzca los segundos: "))
def calcTiempo(horas, minutos,segundos):
    horas= horas*3600
    minutos= minutos*60
    suma= horas+minutos+segundos
    print("la suma es ",suma)
calcTiempo(horas, minutos,segundos)    
'''
'''7. Escriba un programa que haga lo contrario al ejercicio anterior.

segundos = int(input("Introduzca la cantidad total de segundos: "))
def calcSegundos(segundos):
    horas = 0
    minutos = 0
    while segundos >= 3600:
        segundos = segundos-3600
        horas+=1
    while segundos >= 60:
        segundos-=60
        minutos+=1

    print("Horas: ",horas," Minutos: ",minutos," Segundos: ",segundos)
calcSegundos(segundos)       
'''

'''8.Escriba un programa que convierta euros en dólares, y otro que convierta dólares en euros

opcion= int(input("0 para convertir Dolar->Euro || 1 para convertir Euro->Dolar: "))
def conversionDolar(euro):
    resultado= euro * 1.11
    print("El resultado de la conversión son ",resultado," $.")
def conversionEuro(dolar):
    resultado= dolar * 0.90
    print("El resultado de la conversión son ",resultado," €.")
    
def conversion(opcion):
    if opcion==0:
        dolar= int(input("Introduzca la cantidad de dólares: "))
        conversionEuro(dolar)
      
    elif opcion==1:
        euro= int(input("Introduzca la cantidad de euros: "))
        conversionDolar(euro)
conversion(opcion)
'''
'''
11. Rehaga el ejercicio 3 con 3 números

num1= int(input("Introduzca el primer número: "))
num2= int(input("Introduzca el segundo número: "))
num3= int(input("Introduzca el tercer número: "))
def intercambioNum(num1,num2,num3):
    numMayor= 0
    if num1>num2 and num1>num3:
        numMayor= num1
    elif num2>num1 and num2>num3:
        numMayor= num2
    elif num3>num1 and num3> num2:
        numMayor= num3
    elif num1==num2 or num2==num3 or num1==num3:
        print("Has introducido dos números iguales")
    #intercambio de valores
    print("Los números valen: ",num1,num2,num3)
    aux=num1
    num1=num2 #el num1 ya tiene el valor de num2
    num2= num3 #num2 tiene el valor de num3
    num3= aux #num3 tiene el valor de num1
    print("El nuevo valor de num1 es: ",num1,", de num2 es ",num2,", de num3 es ",num3)     
    print("El número mayor es: ",numMayor)
intercambioNum(num1, num2,num3)
'''
'''
Escriba un programa que calcule el equivalente en pies de una longitud en metros dada por el usuario,
teniendo en cuenta que un metro equivale a 39,37 pulgadas y que 12 pulgadas equivalen a un pie. 

#1 metro equivale a 3.281 pies
def calcPie(metros):
    resultado = metros * 3.281
    print(resultado)

metros= int(input("Introduzca los metros a convertir: "))
calcPie(metros)
'''
'''13. Escriba un programa que convierta grados Celsius en Fahrenheit y viceversa,
a elección del usuario. La relación entre ambos es F=(9/5)*C+32. 
opcion = int(input("Elija la opción: \n1.Convertir a Celsius \n2.Convertir a Fahrenheit \n0.Para salir "))
def menu(opcion):
    while opcion != 0:
        if opcion==1:
            conversionACelsius()
        if opcion ==2:
            conversionAFahrenheit()
        opcion = int(input("Elija la opción: \n1.Convertir a Celsius \n2.Convertir a Fahrenheit \n "))
def conversionACelsius():
    grados= int(input("Indica los grados Fahrenheit que desea convertir: "))
    grados = (grados-32)* 5/9
    print(grados)
    return 
def conversionAFahrenheit():
    grados= int(input("Indica los grados Celsius que desea convertir: "))
    grados= (grados * 9/5)+32
    print(grados)
    return   
menu(opcion)
'''
'''
14. Escriba un programa que calcule el valor absoluto de un número.

num= int(input("Introduzca un número para conocer su valor absoluto: "))
print("El valor absoluto de ",num," es ",abs(num))
'''
'''
15. Escriba un programa que calcule si un año es bisiesto. Un año es bisiesto si es múltiplo de 4 pero no de 100 aunque sí de 400. 

anio=int(input("Introduce el año: "))
def calculoBisiesto(anio):
    if anio % 4 == 0 and anio % 4 == 0 and anio % 100 != 0:
        print("el año es bisiesto")
    else:
        print("el año no es bisiesto")
calculoBisiesto(anio)
'''
'''16. Escriba un programa que lea por teclado 20 números reales y
calcule su media. Hacerlo sin utilizar 20 variables reales.

def media():
    contador = 0
    suma = 0
    for i in range(0,20):
        num= int(input("Introduzca el numero: "))
        suma += num
        contador+=1
    print("La suma de los numeros es: ",suma," y su media es ",suma/contador)
media()
'''
'''
17. Escriba un programa que pida dos números enteros y nos muestre
la tabla de multiplicar del primero hasta el número que indique el segundo

num1= int(input("Introduzca el primer número " ))
num2= int(input("Introduzca el segundo número " ))
def tablaMultiplicar(num1, num2):
    for i in range(num1, num2):
        print()
    
'''
'''
 18. Se definen los números triangulares como los obtenidos
 de sumar los números naturales sucesivos 1, 2, 3 …
 Es decir, los primeros números triangulares son 1, 3, 6, 10, etc.
 Escriba un programa que nos diga si un número es o no triangular

x = int(input("Escribe número a comprobar: "))
i, aux, anterior, valido = 1, 2, 0, False

while i <= x:
 print("al princio del while i vale ",i,"x vale ",x)   
 if i+aux < x:
  print("estoy en el if")
  anterior = i
  print("anterior vale ",anterior)
  i = i + aux
  print("i vale ",i)
  aux += 1
  print("aux vale ",aux)
 elif i+aux == x:
  print("estoy en el elif")
  anterior = i
  print("anterior vale ",anterior)
  i = i + aux
  print("i vale ",i)
  aux += 1
  print("aux vale ",aux)
  valido = True
 else:
  break

if valido:
 print(x, ' es un número triangular')
 print('El anterior número triangular es ', anterior)
 print('El siguiente número triangular es ', str(i + aux))
else:
 print(x, ' no es un número triangular')
 print('El anterior número triangular es ', i)
 print('El siguiente número triangular es ', str(i + aux))
'''

'''
19. Escriba un programa que muestre los N primeros números triangulares. 

num = int(input("Introduzca cuántos números triangulares quiere visualizar: "))

i=1
aux=2
#bucle que va hasta num
for j in range(0, num):
    print(i)
    i= i+aux
    aux+= 1
'''
'''
20. Escriba un programa que calcule el factorial de un número.

num1= int(input("Introduzca el primer número " ))
def factorial(num1):
    #factorial empieza en el 1
    resultado=1
    for i in range(1, num1):
        print("i es ",i,"res es ",resultado)
        resultado += (i * resultado)
        print("i es ",i,"res es ",resultado)
    print(resultado)
factorial(num1)
'''
'''
21. Escriba un programa que muestre por pantalla todos
los divisores de un número.

num=int(input("Introduzca un número para conocer sus divisores: "))
for i in range(1,num):
    if num%i==0:
        print(i," es divisor")
'''

'''
22. Un número entero se dice perfecto si es igual a la suma de sus divisores
(excepto él mismo, pero incluyendo el 1). El primer número perfecto es 6: 6=1+2+3.
Escriba un programa que visualice los 4 primeros números perfectos.
'''
'''
x = int(input('Escribe un número: '))

r = 0
for i in range(1, x):
    if x % i == 0:
        r = r + i

if r == x:
    print('Es un número perfecto')
else:
    print('No es un número perfecto...')
'''

'''
for i in range(2,8200):
    suma=0
    for j in range(1,(i//2)+1):
        if(i%j==0):
            suma= suma+j
    if(suma == i):
        print("El número ",i," es perfecto")
'''














        
        
