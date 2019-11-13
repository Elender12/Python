#ejercicio marinero
print("El marinero MiniGarf necesita tu ayuda.")
#num = int(input("Introduzca un número para ayudarlo: "))
contPasosRectos=0
contPasoLatDerecha=0
contPasoLatIzquierda=0
#primero verificamos si se duerme o no
#no se ha dormido y da pasos
while (contPasosRectos <16 and contPasoLatDerecha <2 and contPasoLatIzquierda <2):
    num = int(input("Introduzca un número para ayudarlo: "))
    if (num > 0):
    #da paso hacia delante
        if (num%2==0): 
            contPasosRectos+=1
            print("MiniGarf ha dado un pasito hacia delante (｡◕‿◕｡) y lleva ya"
              ,contPasosRectos," pasitos")
            if(contPasosRectos == 16):
                print("MiniGarf ha llegado al barco ヾ(⌐■_■)ノ♪")
                break;
        
    #pasos hacia los laterales
        else:
            if((num-1)%4==0):
                contPasoLatDerecha+=1
                print("MiniGarf ha dado un pasito hacia la derecha (◉_◉) y lleva ya ",
                  contPasoLatDerecha," pasitos.")
            elif((num-1)%4!=0):
                contPasoLatIzquierda+=1
                print("MiniGarf ha dado un pasito hacia la izquierda (ʘᗩʘ') y lleva ya "
                  ,contPasoLatIzquierda," pasitos")
            if(contPasoLatDerecha == 2 or contPasoLatIzquierda == 2):
                print("Ohh...MiniGarf se ha caído por la rampa")
    #se duerme
    else:
        print("MiniGarf se ha dormido sobre la rampa (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ zZzZzZzZz")
        break;
    
    
