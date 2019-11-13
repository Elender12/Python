'''
 1. Escribe un programa que traduzca un número romano menor que 4000
 a un número en caracteres arábigos y viceversa.
'''     
def convertirRomanoArabigo():
#leo el número formato String
 numRomano = input("Introduzca un número a convertir: ")
#print(num)
#variables a utilizar
 valores = {
  'I': 1,
  'V': 5,
  'X':10,
  'L':50,
  'C':100,
  'D':500,
  'M':1000
 }
 val_Ant = 0
 suma=0
#hay un valor actual, uno anterior y uno siguiente?

 if len(numRomano) > 0:
    #es la primera letra
     val_Inicial = numRomano[0]
     #print(val_Ant)
 else:
     print("No has introducido nada")
 for letra in numRomano:
    val_Ant= valores[val_Inicial]
 for letra in numRomano:
   if letra in valores:
        val_Act= valores[letra]
        if val_Ant >= val_Act:
            suma += val_Act
        else:
            suma += (val_Act- (2* val_Ant))
            #varTest = (val_Act-val_Ant)
        val_Ant= val_Act
   else:
        print("cacho burro, aprende a escribir el letras romanas")
 print("El resultado es: ",suma)

def convertirArabigoRomano():
 numArabe= int(input("Introduzca el número arábigo: "))
 miles=0
 centenas=0
 numRomano=""
 while(numArabe>999):
      numArabe -=1000 #le hemos quitado 1000 -
      #miles= miles + 1
      numRomano+= "M"
 #if(numArabe>999):
 if(numArabe>=900 and numArabe <=999):
      numArabe-=900
      numRomano+="CM"
 #if(numArabe>=800 and numArabe <=888):
 if(numArabe>500):
      numArabe-=500 #le quitamos 500
      numRomano +="D"
      print(numArabe)
 if(numArabe>= 400 and numArabe <=499):
      numArabe -=400
      numRomano += "CD"        
 while(numArabe<399 and numArabe > 99):
      numArabe-=100
      numRomano+="C"
      #if(numArabe )
      #print("numero arabe despues de la resta de centenas",numArabe)
 if(numArabe <= 99 and numArabe >=90):
     numArabe-=90
     numRomano+="XC" #este es 90
 if(numArabe >=50):
     numArabe-=50
     numRomano+="L" #este es 50
 if(numArabe >=40 and numArabe<=49):
           numArabe-=40
           numRomano+="XL"
 else:
      while(numArabe <=39 and numArabe >= 10):
           numArabe-= 10
           numRomano+="X"
 if(numArabe == 9):
      numArabe-=9
      numRomano+="IX"
 elif(numArabe >=5 and numArabe<9):
      numArabe -= 5
      numRomano+="V"
 elif(numArabe == 4):
      numArabe-=4
      numRomano+="IV"
 while(numArabe < 4 and numArabe > 0):
       numArabe-= 1
       #print(numArabe,"num arabe dentro del ultimo while")
       numRomano+="I"
       #print("no explotes porfis")              
 print("El número romano es ", numRomano)
print("1. Para convertir un número romano a arábigo. \n2. Para convertir número arábigo a romano. \n0 Para salir")
opcion= int(input())
while(int(opcion)!= 0):
     if(opcion == 1):
          convertirRomanoArabigo()
     if(opcion==2):
          convertirArabigoRomano()
     print("1. Para convertir un número romano a arábigo. \n2. Para convertir número arábigo a romano. \n0 Para salir")
     opcion= int(input("Introduzca de nuevo su opcion: "))
     







    
