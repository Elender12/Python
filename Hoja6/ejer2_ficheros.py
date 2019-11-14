'''
2. Escribe un programa que analice el fichero de texto cuyo nombre
se especifica interactivamente y muestre por pantalla la siguiente información:
a) Para cada línea del fichero:
• El número total de caracteres y de palabras, y la longitud media de una palabra.
• La letra con que termina la primera palabra y el número de palabras que terminan con esa letra.
b) Para el fichero completo:
• El número total de caracteres, palabras y líneas del fichero, y la longitud media
de una palabra.
• El número de la línea en la que hay más palabras, junto con el número de palabras
en esa línea.

El número de la línea en la que hay más palabras que acaban como la primera,
junto con el número de esas palabras.
'''
import pathlib
#import numpy

#el usuario introduce el fichero a buscar también con el formato incluido
nombre= input("Introduce el nombre del fichero(con su extensión incluida): ")

#verifico que el archivo exista
resul = pathlib.Path(f"{nombre}")
if resul.exists ():
    print ("El fichero existe. Todo continua.")
    print("Abriendo ",resul,"...")
    file = open(resul,"r+")
    
else:
    print ("El fichero no existe.")

data = file.read()
linea= file.readline();
print(linea)
file.seek(0)
    
'''
a) Para cada línea del fichero:
• La letra con que termina la primera palabra y el número de palabras que terminan con esa letra.
'''
def numCaracLinea(resul):
     with open(resul) as fp:
       fp.seek(0)
       #contador para mostrar las palabras que terminan en la misma letra MENOS la primera
       cnt = -1
       #variables a utilizar
       palabra=""
       ultimaLetra1=""
       #bucle en el cual leo cada linea
       for i in fp:
           #almaceno las palabras en un array
           palabra= i.split()
           #imprimo las listas de palabras
           print("Lista de palabras",palabra)
           #saco la primera palabra
           primeraPalabra = palabra[0]
           print("La primera palabra es ",primeraPalabra)
           #muestra la última letra
           ultimaLetra1= primeraPalabra[len(primeraPalabra)-1:]
           print("La última letra es: ",ultimaLetra1)
           #mirar cuántas palabras terminan con la última letra
           for j in palabra:
               #print("palabra j",j)
               letra= j[len(j)-1:]
               if letra==ultimaLetra1:
                    cnt+=1
           print("hay ",cnt," palabras que terminan en ",ultimaLetra1)
           print("\n")
           #reinicio el contador para que muestre las palabras de cada fila
           cnt=-1


#El número total de caracteres y de palabras, y la longitud media de una palabra.
def numPalabras(resul):
    with open(resul) as fp:
        fp.seek(0)
        palabra=""
        cnt=0
        cntCarac=0
        media=0
        mayor= []
        aux = 0
        for linea in fp:
            #separo cada línea y almaceno sus palabras
            palabra = linea.split()
            #cuento el número de línea
            cnt+=1
            #imprimo los datos
            #meter una variable auxiliar de máximo
            aux= len(palabra)
            
            mayor.append(aux)
            print("línea ",cnt," tiene ",len(palabra)," palabra/s")
            #recorro las palabras de cada línea y las sumo
            for letra in palabra:
                cntCarac +=len(letra)
            #imprimo los datos
            print("Hay un total de ",cntCarac," letras.")
            media= cntCarac/len(palabra)
            print("La longitud media de una palabra es ","{0:.1f}".format(media))
            print("\n")
            #restablezco el contador para que no vaya acumulando todos los datos
            cntCarac=0
        print(mayor)
       
        for i in range (1, len(mayor)):
            if max(mayor)== mayor[i]:
                 print("La línea con más número de palabras es ",i+1, "con ",max(mayor)," palabras")
           

            
            
print("PARA CADA LÍNEA DEL FICHERO: ")
numCaracLinea(resul)
numPalabras(resul)



'''
a) Para todo el fichero:
• El número total de caracteres y de palabras, y la longitud media de una palabra.
'''
#cuenta los caracteres
def cuentaCaracteres(file):
    contador=0
    for linea in data:
        contador+=1
    #print("Hay ",contador," caracteres")
    return contador

#cuenta las palabras
def cuentaPalabras(file):
    lista = [];
    palabra = "";
    palabra= data.split()
    lista.append(palabra)
    return lista

#calculo la longitud media de una palabra
print("----------------------------------------------")
print("----------------------------------------------")
print("PARA TODO EL FICHERO: ")
numPalabras= []
numPalabras= cuentaPalabras(data)
contadorLetras= cuentaCaracteres(data)
longitud= contadorLetras/(len(numPalabras[0]))
print("Hay ",len(numPalabras[0])," palabras con un total de ",contadorLetras," letras y la longitud media de una palabra es ","{0:.1f}".format(longitud)," caracteres")

'''
•La letra con que termina la primera palabra y el número de palabras que terminan con esa letra.
'''
def ultimaLetra(data):
    letra=""
    palabras=""
    contador=0
    #esto ya es una lista en si
    palabras= data.split()
    #muestra la última letra
    for i in palabras[0]:
        letra= i[len(i)-1]
    for j in palabras:
        if letra == j[len(j)-1]:
            #print(j)
            contador+=1    
    #print("La letra es ",letra," y hay ",contador," palabras")

'''
• El número de la línea en la que hay más palabras, junto con el número de palabras
en esa línea.
'''





    
#ultimaLetra(data)

file.close()
'''
#buscaPalabra(data)
def buscaCaracteres(file):

    for line in file:        
        palabra= line.split()            
        lista.append(palabra)
    print(lista)
    return lista
'''
