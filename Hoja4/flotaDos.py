import random
#-----PREPARACIÓN DEL JUEGO--------
#matriz usuario
matrizUsuario= [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
#matriz ordenador
matrizOrdenador= [[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0]]
#aquí guardo los disparos que se han realizado
auxUsuario= [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
auxOrdenador=[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
def mostrarMatriz(matriz):
      for i in range(len(matriz)):
        for j in range(len(matriz)):   
            print(" {0} ".format(matriz[i][j]), sep=',', end='')
        print('\n')
print("Cargando juego..........")
print("........................")
#-----------MAKINA ELIGE SU BARCO----------
#elegir posiciones aleatorias para el ordenador
def barcoOrdenador(matrizOrdenador):
    fila1= random.randint(0,4)
    columna1=random.randint(0,4)
    num= 7
    filas= len(matrizOrdenador)
    columnas= len(matrizOrdenador[0])
    print('Makina ha posicionado su barco. ')
    print('fila: ',fila1)
    print('columna: ',columna1)
    #print(num)
    for i in range(filas):
        for j in range(columnas):
            if matrizOrdenador[i][j]== matrizOrdenador[fila1][columna1]:
                #asigna el número aleatorio como barco
                matrizOrdenador[fila1][columna1] = num
                matrizOrdenador[fila1][columna1+1] = num+1
           # if matrizOrdenador[i-1][j-1]== matrizOrdenador[fila1-1][columna1-1]:
             #   matrizOrdenador[i-1][j-1] = num-1
    
    return matrizOrdenador
print("debajo está la función de mostrar matriz")


barcoOrdenador(matrizOrdenador)
mostrarMatriz(matrizOrdenador)

#--------USUARIO ELIGE SU BARCO-----------
#barco que elige el usuario
def barcoUsuario(matrizUsuario):
    fila= int(input("Usuario, elige la fila donde quieres poner tu barco: "))
    columna= int(input("Usuario, elige la columna donde quieres poner tu barco"))
    print('Usuario ha posicionado su barco: ')
    for i in range(len(matrizUsuario)):
        for j in range(len(matrizUsuario)):
            if matrizUsuario[i][j]== matrizUsuario[fila-1][columna-1]:
               matrizUsuario[fila-1][columna-1]=7    
            print(" {0} ".format(matrizUsuario[i][j]), sep=',', end='')
        print('\n')
    return matrizOrdenador



barcoUsuario(matrizUsuario)
#--------------EMPIEZA EL JUEGO----------------------
#numeros que da el usuario para la posicion
def turnoUsuario(auxUsuario):
 posFilaU= int(input(" Usuario, introduce la fila a disparar: "))
 while posFilaU > 5 or posFilaU < 0:
         posFilaU= int(input(" Usuario, introduce una fila VÁLIDA a disparar: "))
 posColumnaU= int(input("Ahora la columna a disparar: "))
 while posColumnaU > 5 or posColumnaU < 0:
         posColumnaU= int(input(" Usuario, introduce una columna VÁLIDA a disparar: "))

 auxUsuario[posFilaU][posColumnaU]="D"
 print("Sitios donde ha disparado el Usuario")
 mostrarMatriz(auxUsuario)

 return (posFilaU,posColumnaU)
#posicionesDisparoUsuario = turnoUsuario()
disparoU = False
disparoM= False
#disparos de Makina
def turnoMakina():

 posFilaO=random.randint(0,4)
 posColumnaO=random.randint(0,4)
 
 return (posFilaO, posColumnaO)

#verifico si el usuario ha acertado el tiro
#def disparoUsuario(matrizOrdenador,posFilaU,posColumnaU):
def disparoUsuario(matrizOrdenador, posicionesDisparoUsuario ):
    if matrizOrdenador[posicionesDisparoUsuario[0]][posicionesDisparoUsuario[1]] !=0:
        print("Makina dice: Tocado Auch... (x_X)")
        disparoU = True
    else:
        print("Makina dice: Mehhh NO tocado")
        disparoU = False
    return disparoU

#disparoU= disparoUsuario(matrizOrdenador,posicionesDisparoUsuario)

#posicionesDisparoMakina = turnoMakina()
def disparoMakina(auxOrdenador):
    
    posFilaO=random.randint(0,2)
    posColumnaO=random.randint(0,2)
    print("dentro del turno de Makina")
    auxOrdenador[posFilaO][posColumnaO]="D"
    print("Sitios donde ha disparado Makina")
    mostrarMatriz(auxOrdenador)

    #print("Los disparos son: ",disparos)
    print('Makina ha disparado en la fila',posFilaO,' y en la columna', posColumnaO)
    print('¿ Te ha dado?')
    respuesta = input("escribe s/n: ")
    if respuesta == "s" and matrizUsuario[posFilaO][posColumnaO] != 0:
            print("Makina ha tocado")
            disparoM= True
    elif matrizUsuario[posFilaO][posColumnaO] !=0 and respuesta == 'n':
            print("No hagas trampas, cacho humano")
            disparoM= False
    else:
            print("Makina no ha tocado")
            disparoM= False
    return disparoM

#disparoM= disparoMakina()
#print("Resultado usuario ",disparoU)
#print("Resultado Makina ",disparoM)

#------SERIE DE DISPAROS--------
while disparoU == False or disparoM == False:
    posicionesDisparoUsuario= turnoUsuario(auxUsuario)
    disparoU= disparoUsuario(matrizOrdenador,posicionesDisparoUsuario)
    if disparoU== True:
        print("Usuario ha ganado")
        break
    mostrarMatriz(matrizUsuario)
    disparoM=disparoMakina(auxOrdenador)
    if disparoM == True:
        print("Makina ha ganado")
        break

#------OTRAS FUNCIONES----------
