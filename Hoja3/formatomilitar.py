'''
2. Escribe un programa que acepte una hora en formato militar y la transforme
al formato habitual (horas, minutos y AM/PM) y viceversa
'''
def formatoMilitarAHabitual():
  formato=input("Introduce la hora en formato militar: ")
  hora= int(formato[0:2])
  minutos=int(formato[2:])
#print(hora, minutos)
#verifico que las horas introducidas sean las correctas
  while(hora>24 or hora< 0 and minutos>59 or minutos< 0 or len(formato)!=4):
    print("Has introducido un formato erróneo.")
    formato=input("Introduce la hora en formato militar: ")
    hora= int(formato[0:2])
    minutos=int(formato[2:])
#hago la conversión
  if(hora<=23 and hora>12):
    hora-=12
    print(hora,":",minutos,"PM")
  else:
    print(hora,":",minutos,"AM")
#la otra función :)
def formatoHabitualAMilitar():
 formato=input("Introduce la hora en formato habitual: (hh:mm AM/PM) ")
 #print(len(formato))
 if(len(formato)== 7):
     #lo lleno con 0 por la izquierda
     formato=formato.zfill(8)
 #print("imprime el formato zfill?",formato)
 hora= int(formato[0:2])
 minutos=int(formato[3:5])
 antePost= formato[6:]
 if(antePost =="PM"):
     hora+=12
     print(str(hora)+str(minutos))
 else:
     print(str(hora)+str(minutos))
print("Elige una opcion: \n1.Covertir desde el formato militar al habitual \n2.Convertir desde el formato habitual al militar \0 para salir ") 
opcion=int(input())
while(opcion!=0):
    if(opcion ==1):
      formatoMilitarAHabitual()
    if(opcion==2):
      formatoHabitualAMilitar()
    opcion=int(input())
