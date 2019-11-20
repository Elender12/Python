from tele import Tele
tele = Tele("Panasonic","RX17",2014)

tele.encender()
#tele.obtenerCanal()
#tele.bajarCanal()
tele.seleccionarCanal(23)
tele.subirCanal()
tele.cambiarVolumen(300)
tele.cambiarVolumen(50)
tele.apagar()
tele.seleccionarCanal(60)
tele.apagar()
tele.imprimirCaracteristicas()