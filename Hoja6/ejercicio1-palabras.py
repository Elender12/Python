'''
Ejercicio 1. Crea un fichero y escribe una palabra (en cualquier idioma)
que no tenga una traducción clara en otros idiomas.
Cierra el fichero. Vuelve a abrir el fichero y agrega su
significado y el idioma de donde proviene.
'''

#abro el fichero
file = open("C:\\Users\\Elena Cirstea\\Documents\\Python\\Ficheros\\palabras.txt","w+")
#escribo dentro
file.write("\nTOSKA: ")
#lo cierro
file.close()

#lo vuelvo a abrir
file = open("C:\\Users\\Elena Cirstea\\Documents\\Python\\Ficheros\\palabras.txt","a+")
#vuelvo a escribir
file.write("(ruso) Una sensación de enorme angustia espiritual, a menudo sin una causa específica; un anhelo sin que haya nada que anhelar")
#file.write("\nMAMIHLAPINATAPEI: un cruce de miradas cargado de significado, sin palabras, entre dos personas que desean iniciar algo, aunque se resisten a hacerlo ")
#leo y lo cierro
file.seek(0)
print(file.read())
file.close()
 
