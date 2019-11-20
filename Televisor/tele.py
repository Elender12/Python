class Tele:
    #empty constructor
    #constructor with parameters
    def __init__(self, marcaInicial, modeloInicial, anioIni):
        self.marca= marcaInicial
        self.modelo=modeloInicial
        if anioIni>2200 and anioIni <1950:
            self.anio= 2000
        else:
            self.anio=anioIni
        self.panoramica= False
        self.stereo=False
        self.encendida=False
        self.volumen=0
        self.canal=0
        pass
    #methods 
    def encender(self): 
        self.encendida= True
        print("Se ha encendido")
        return self.encendida
    def apagar(self):
        self.encendida= False
        print("Se ha apagado")
        return self.encendida
    def seleccionarCanal(self, nuevoCanal):
        if self.encendida == True:
            if nuevoCanal<= 99 and nuevoCanal>=0:
             self.canal= nuevoCanal
             print("El canal es ", self.canal)
            else:
             print("Ha introducido un canal que no es válido.")
        else:
            print("El televisor está apagado.")
       
    def obtenerCanal(self):
        if self.encendida == True:
            print("El canal es ", self.canal)
            return self.canal
        else:
            print("Televisor apagado.")
    #def setAnio(self):

    def subirCanal(self):
        if self.encendida == True:
            if self.canal == 99:
                print("No se puede subir de canal (x_X)")
            else:
                self.canal+=1
        else:
            print("Televisor apagado.")
    def bajarCanal(self):

        if self.encendida == True:
            if self.canal== 0:
                print("Error!!! no se puede bajar de canal x_X")
            else:
                self.canal-=1
        else:
            print("Televisor apagado.")
    def cambiarVolumen(self,nuevoVolumen):
        if self.encendida == True:
            if nuevoVolumen<=100 and nuevoVolumen>=0:
                self.volumen=nuevoVolumen
                print("El nuevo volumen es: ",self.volumen)
            else:
             print("El volumen introducido no es válido.")
        else:
            print("Televisor apagado.")
   
    def imprimirCaracteristicas(self):
        print("La marca es ",self.marca," del modelo ",self.modelo, " y el año ",self.anio)
        print("Panorámica: ",self.panoramica,", stereo: ",self.stereo,", nivel de volumen: ", self.volumen, ", canal: ", self.canal)

