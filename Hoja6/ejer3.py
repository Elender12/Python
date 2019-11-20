'''
Ejercicio 3. Dada una palabra, diremos que está escondida en un texto si está contenida en éste, no necesariamente de forma continua.
Por ejemplo, la palabra “elefante” está escondida en la frase “El hermano de Francisco tuvo suerte”.
elabora un programa que lea una palabra de teclado y el nombre de un fichero de texto, y mire a ver si la palabra está escondida en el fichero.
Si está nos debe de indicar el menor número de carácter en el que ya está contenida. Si no está nos tiene también que informar de esa incidencia.
La palabra a buscar no tendrá más de 50 caracteres, pero desconocemos su longitud.
'''

import pathlib

#el usuario introduce el fichero a buscar también con el formato incluido
nombre= input("Introduce el nombre del fichero(con su extensión incluida): ")

#verifico que el archivo exista
archivito = pathlib.Path(f"{nombre}")
if archivito.exists ():
    print ("El fichero existe. Todo continua.")
    print("Abriendo ",archivito,"...")
    file = open(archivito,"r+")
    
else:
    print ("El fichero no existe.")
data = file.read()
linea= file.readline();
#print(linea)
file.seek(0)
palabraEscondida = input("Introduce la palabra a verificar si existe: ")
if len(palabraEscondida)>50:
    print("no vale")
else:
    buscarPalabra(file, palabraEscondida)
def buscarPalabra(file, palabraEscondida):
    palabra = "";
    lista = []
    existe = False
    #almaceno las palabras del fichero en un array
    palabra= data.split()
    #print(palabra)
    #print(palabraEscondida[0])
    for i in range(0, len(palabraEscondida)):
        veces= palabraEscondida.count(palabraEscondida[i])
        #print(veces,"veces",palabraEscondida[i])
        #me imprime cada letra con cada bucle
        #print(palabraEscondida[i])
        for pal in palabra:
            #me imprime todas las palabras del texto
            for j in range(0, len(pal)):
                if palabraEscondida[i]== pal[j]:
                    if palabraEscondida[i] not in lista:
                        lista.append(palabraEscondida[i])
                        #print(lista,"en el if")
                        break
                    if veces>1 and lista.count(palabraEscondida[i]) < veces:
                        lista.append(palabraEscondida[i])     
    #print(lista)
    if len(lista) == len(palabraEscondida):
        existe= True
    else:
        existe= False
    #lista = list(set(lista))
    print("La palabra está escondida: ",existe)

























