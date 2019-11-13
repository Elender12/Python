#examen tablas multiplicación
import random
respuestaBuena = 0
respuestasMal=0
for i in range(0,10):
    num1 =random.randint(0,10)
    num2= random.randint(0,10)
    resultado = num1*num2
    print(num1," * ", num2)
    resAlumno = int(input("Escribe el resultado: "))
    if (resultado == resAlumno):
        respuestaBuena +=1
    else:
        while(resultado != resAlumno):
            resAlumno = int(input("Escribe el resultado de nuevo: "))
            respuestasMal+=1
print("Enhorabuena, has aprobado con ",respuestaBuena," bien y has fallado en ",
      respuestasMal," preguntas")
            
    
