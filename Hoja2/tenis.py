import random

numMaxSets= int(input("Introduzca el número máximo de sets: "))

#print(random.randint(0, 1))
jugadorA=0
setsGanadosA=0
setsGanadosB=0
jugadorB=0
#para ganar el partido (mitad +1 de los sets)
for i in range(0,numMaxSets):
#para ganar 1 set
    for i in range(0,10):
        ganador = random.randint(0, 1)
        #print("el valor de random es",ganador)
        if(ganador == 1 ):
            jugadorA+=1
            #print("Jugador A",jugadorA)
        else:
            jugadorB+=1
            #print("Jugador B",jugadorB)
    #print("El jugador A ha ganado ",jugadorA," juegos")
    #print("El jugador B ha ganado ",jugadorB," juegos")
    if((jugadorA >= 6 and jugadorB <= 4) or jugadorA >=7):
        #print("El jugador A ha ganado el set.")
        setsGanadosA+=1
        jugadorA=0
        #print("sets ganados por jugador A",setsGanadosA)
        #break
    elif((jugadorB >= 6 and jugadorA <= 4) or jugadorB >=7):
        #print("El jugador B ha ganado el set.")
        setsGanadosB+=1
        jugadorB=0
        #print("sets ganados por jugador B",setsGanadosB)
        #break
    else:
        #esto hay que modificarlo
        print("Hay empate")
print("Valor de sets ganados por Jugador A",setsGanadosA)
print("Valor de sets ganados por Jugador B",setsGanadosB)
if(setsGanadosA >= numMaxSets//2+1):
    print("ha ganado el jugador A!!!!!")
if(setsGanadosB >= numMaxSets//2+1):
    print("ha ganado el jugador B!!!!!")



    
