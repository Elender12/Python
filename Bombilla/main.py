from bombilla import Bombilla
bombilla = Bombilla()
#Encendemos y apagamos mil veces
for i in range(1000): 
    bombilla.encender()
    bombilla.apagar()
bombilla.encender()
num= bombilla.getVecesEncendidas()
num2= bombilla.getVecesApagadas()
# if num==1000 and num2== 1000:
#     print("Se ha fundido")
#     bombilla.encender()
estado = bombilla.getEstado()

print("El estado actual de su bombilla es: ",estado)

#bombilla.apagar() 
#Y otra vez más, aunque debería estar fundida y   a
#bombilla.encender()
#bombilla.apagar()
