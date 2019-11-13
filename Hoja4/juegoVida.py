'''
Que comience el juego de la vida
* triciclo de JigSaw pasando de fondo *
'''
import random
import sys
vecinoUniversal = 0

def crearBichitosAleatorios():
    #numFilas= 0
    vecino = 0
    #numColumnas = 0
    tablero, numFilas, numColumnas = crearTablero()
    conjuntoB= 0
    fila = random.randint(1, numFilas-1)
    columna= random.randint(1,numColumnas-1)
    
    #print("fila: ",fila, " columna: ",columna)
    #print("fila1: ",fila1, " columna1: ",columna1)
    tablero[fila][columna] = '*'
    #if tablero[fila+1]>0:
    
    '''
    try:
        tablero[fila+1][columna+1] = '*'
    except IndexError:
        tablero[fila1][columna1] = '*'
        print("se va del index a.k.a. madre pero se ha solucionado")
        pass
    '''
    while conjuntoB<2:
        for i in range(fila-1,fila+2):
            for j in range(columna-1,columna+2):
                fila1 = random.randint(1, numFilas-1)
                columna1= random.randint(1,numColumnas-1)
                try:
                    tablero[fila+1][columna-1] = '*'
                    tablero[fila-1][columna+1] = '*'
                    tablero[fila+1][columna+1] = '*'
                #tablero[i][j] 
                    #print("conjunto creado")
                    conjuntoB+=1
                except IndexError:
                    tablero[fila1][columna1] = '*'
                    #print("se va del index a.k.a. de madre pero se ha solucionado")
                    #print("bichito random generado por la tabla")
                    conjuntoB+=1
                    pass    

    vecino = mirarOtroVecino(tablero, fila, columna)
    if vecino==3:
        if tablero[fila1][columna1] == 0:
            tablero[fila1][columna1]='*'
            #print("ha nacido un bichito") 
    #verTablero(tablero)
    return tablero
        
def crearTablero():
    print("Vamos a definir las medidas del tablero: ")
    numFilas= int(input("Introduce el número de filas: "))
    while numFilas< 3:
        print("No se puede crear bichitos en un espacio tan pequeño")
        numFilas= int(input("Introduce DE NUEVO el número de filas: "))  
    numColumnas= int(input("Introduce el número de columnas: "))
    while numColumnas < 3:
        print("No se puede crear bichitos en un espacio tan pequeño")
        numColumnas= int(input("Introduce DE NUEVO el número de filas: "))
    print("Has creado el nuevo universo para los bichitos.")
#relleno tablero de 0
    tablero= []
    tablero = [[0 for x in range(numFilas)] for y in range(numColumnas)]
    
    return tablero, numFilas, numColumnas

#imprimir el tablero
def verTablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
          print(" {0}  ".format(tablero[i][j]), sep=',', end='')
        print('\n')
#tablero = crearTablero()
#llamo a la función para ver el tablero
#verTablero(tablero)
#print("solo para verificar")

#borrar bichito
def borrarBichito(tablero):
    print("Vamos a borrar un bichito :(")
    posFila= int(input("Introduce la posición de la fila: "))
    posColumna= int(input("Introduce la posición de la columna: "))
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            #verifico que las columnas existan y que hay un bichito allí
            if tablero[i][j]== tablero[posFila][posColumna] and tablero[posFila][posColumna] == '*':
                tablero[posFila][posColumna]= 0
                #print("¡¡¡¡Bichito borrado!!!")
    return tablero

#vamos a crear un bichito
def crearBichito(tablero):
    global vecinoUniversal
    vecinoUniversal=0
    print("Vamos a crear un bichito (^^,)")
    posFila= int(input("Introduce la posición de la fila: "))
    posColumna= int(input("Introduce la posición de la columna: "))
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j]== tablero[posFila][posColumna] and tablero[posFila][posColumna] != '*':
                try:
                 tablero[posFila][posColumna]= '*'
                #tablero[posFila][posColumna]=  "\U0001F41B"
                 #print("¡¡¡¡Bichito creado!!!\U0001F41B")
                except IndexError:
                    pass
    vecinoUniversal+=mirarOtroVecino(tablero, posFila,posColumna)
    #print("vecino desede crearBichito()",vecinoUniversal)
    #return tablero
    return tablero,posFila,posColumna


def mirarOtroVecino(tablero, posBfila,posBcol):
    vecino = 0
    for i in range(posBfila-1,posBfila+2):
        for j in range(posBcol-1,posBcol+2):
            try:
                if tablero[i][j]== "*" and (i!= posBfila or j!=posBcol):
                    #print("Vecino desde la función de otro vecino.")
                    vecino+=1
            except IndexError:
                    pass
    #print("valor vecino en la función mirarOtroVecino ",vecino)
    return vecino


#función que intentará mirar cuántos vecinos tiene un elemento, para ver si puedo simular una generación
def buscarVecinoUniversal(tablero):
    auxTablero= []
    contadorVecino=0
    auxTablero = tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            fila1 = random.randint(1,len(tablero)-1)
            columna1= random.randint(1,len(tablero)-1)
            if tablero[i][j]== "*":
                #print("Bicho found!\U0001F41B. Ahora a buscar sus vecinos")
                contadorVecino=mirarOtroVecino(tablero, i,j)
                #verTablero(tablero)
                #print("Estoy mirando los vecinos del bichito en la posicion ",i,j)
                #print("número de vecinos: ",contadorVecino)
                
                if contadorVecino == 3:
                    print("Va a nacer un bichito nuevo \U0001F41B")
                    #tablero[fila1][columna1]='N'
                    
                    auxTablero[fila1][columna1]='*'
                    #verTablero(auxTablero)
                if contadorVecino >=4 :
                    try:
                        print("El bichito en la posición ",i,j," va a morir de agobio...")
                        auxTablero[i][j]= '0'
                        #verTablero(auxTablero)
                    except IndexError:
                        pass 
                #break
            else:
                continue
    return auxTablero,tablero
    

#------------MENÚ---------
opcion=1
vecino = 0
while opcion !=0:
    opcion= int(input("Elige tu opción: \n1. Nuevo tablero con bichos aleatorios \n2. Tablero en blanco \n3. Crea un bicho \n4. Borra un bicho \n5. Simula un determinado número de generaciones \n0. Salir \n>>"))
    if opcion == 1:
        tablero= crearBichitosAleatorios()
        verTablero(tablero)
    if opcion ==2:
        tablero, posFila, posColumna = crearTablero()
        verTablero(tablero)
    if opcion == 3:
        tablero, posFila, posColumna = crearBichito(tablero)
        #vecino = mirarOtroVecino(tablero, posFila,posColumna)
        #print("vecino Universal desde fuera: ",vecinoUniversal)
        verTablero(tablero)
        #mirarVecino(tablero)
    if opcion ==4:
        tablero = borrarBichito(tablero)
        verTablero(tablero)
    if opcion== 5:
        numGeneraciones= int(input("Introduzca el número de generaciones: "))
        for i in range(0,numGeneraciones):
            tableroAux, tablero1 = buscarVecinoUniversal(tablero)
            print("Generación: ",i+1)
            verTablero(tablero1)
            print("\n")
            print("abajo la tabla auxiliar")
            verTablero(tableroAux)

    
#crearBichito(tablero)
#crearBichito(tablero)
#crearBichito(tablero)

#print("El nuevo tablero: ")

#-------------CÓDIGO OBSOLETO---------------------
    '''
    try:
        tablero[fila-1][columna-1] = '*'
    except IndexError:
        #print("se va del index ak madre del otro try")
        pass
    try:
        tablero[fila+1][columna-1] = '*'
    except IndexError:
        #print("se va del index ak madre del otro try")
        pass
    try:
        tablero[fila+1][columna+1] = '*'
    except IndexError:
        #print("se va del index ak madre del otro try")
        pass
    '''

    '''
def mirarVecino(tablero, posBfila,posBcol):
    vecino = 0
    #posBfila= int(input("Fila del bichito a buscar: "))
    #posBcol = int(input("Columna dei bichito a buscar: "))

    if tablero[posBfila-1][posBcol-1] != 0:
        print("vecino arriba a la izquierda")
        vecino+=1
    if tablero[posBfila-1][posBcol] != 0:
        print("vecino arriba en el medio")
        vecino+=1
    if tablero[posBfila-1][posBcol+1] !=0:
        print("vecino arriba a la derecha" )
        vecino+=1
    if tablero[posBfila][posBcol-1] == tablero[posBfila][posBcol]:
        print("hay un vecino a la izquierda!!!!!")
        vecino+=1
    if tablero[posBfila][posBcol+1] != 0:
        print("vecino a la derecha" )
        vecino+=1
    if tablero[posBfila+1][posBcol-1] != 0:
        print("vecino abajo a la izquierda" )
    if tablero[posBfila+1][posBcol] != 0:
        print("vecino justo debajo" )
        vecino+=1
    if tablero[posBfila+1][posBcol+1] != 0:
        print("vecino abajo a la derecha" )
        vecino+=1
    #else:
        #print("no hay vecino-.-")
    #print("num vecinos",vecino)
    return vecino
#opcion=int(input("Introduce 1 para entrar: "))
'''
