class Coche:
    def __init__(self, matricula, maxLitrosDeposito, consumoMedio, velocidadMax):
        self.matricula = matricula
        if maxLitrosDeposito>0:
            self.maxLitrosDeposito= maxLitrosDeposito
        else:
            self.maxLitrosDeposito=50
        self.maxLitrosReserva= (15 * self.maxLitrosDeposito)/100
        if velocidadMax>0:
            self.velocidadMaxima=velocidadMax
        else:
            self.velocidadMaxima=180
        if consumoMedio>0:
            self.consumoMedio= consumoMedio
        else:
            self.consumoMedio=7.5

    #propiedades que definen el estado del coche
        self.motorArrancado= False
        self.estaEnReserva= False
        #combustible que tiene el coche de normal
        self.numLitrosActual= 0.0
        self.velocidadActual=0.0
        self.kilometraje=0.0
        pass
    # def estarEnReserva(self):
    #     if self.numLitrosActual<= self.maxLitrosReserva and self.numLitrosActual>0:
    #         self.estaEnReserva= True
    #     return self.estaEnReserva
    def arrancarMotor(self):
        if self.numLitrosActual>0:
            print("El coche con matrícula ",self.matricula,"ha arrancado")
            self.motorArrancado= True
        else:
            print("Ohh no, no puede arrancar porque no tiene combustible")
        if self.numLitrosActual<= self.maxLitrosReserva and self.numLitrosActual>0:
            self.estaEnReserva= True
            print("Pero... estás en reserva!")
  
    def pararMotor(self):
        if self.motorArrancado== True:
            self.motorArrancado= False
            print("Motor parado ")
        else:
            print("Mehh no hago nada.")
    def repostarCombustile(self,litros):
        if litros < 0:
            print("mehh no hago nada")
        else:
            self.numLitrosActual+= litros
            if self.maxLitrosDeposito < self.numLitrosActual:
                print("El combustible del tanque se ha ido de madre")
                self.numLitrosActual=self.maxLitrosDeposito
        print("El coche con matrícula ",self.matricula,"tiene disponible ",self.numLitrosActual,"litros de combustile")
    def fijarVelocidad(self, velocidad):
        if self.motorArrancado== True:
            if velocidad> self.velocidadMaxima:
                self.velocidadActual= self.velocidadMaxima
            elif velocidad<0:
                self.velocidadActual=0
            else:
               self.velocidadActual= velocidad
            print("La nueva velocidad es ", self.velocidadActual)
        else:
            print("El coche está parado")
    def recorrerDistancia(self, km):
        #variables necesarias para el método
        consumoActual= self.consumoMedio * (1+(self.velocidadActual-100)/100)
        print(consumoActual,"es el consumo actual")
        litrosNecesarios=  km * (consumoActual/100)
        distanciaReal= 100*self.numLitrosActual/consumoActual
        #si num litros necesarios es menor que deposito se puede recorrer|| actualizar
        if float(litrosNecesarios) < float(self.numLitrosActual):
            print("Se puede recorrer la distancia.")
            print("El coche con matrícula ",self.matricula,"ha recorrido",km,"kilómetros.")
            self.numLitrosActual-= litrosNecesarios
            self.kilometraje= km
            print("num litros actuales:",self.numLitrosActual)
            print(self.maxLitrosReserva)
            if self.numLitrosActual<= self.maxLitrosReserva and self.numLitrosActual>0:
                self.estaEnReserva= True
                print("estás en reserva")
            print("Al coche le quedan en el depósito ",self.numLitrosActual," y está en reserva",self.estaEnReserva)
        else:
            print("ehmm no puedes recorrer esta distancia")

        #print("litros necesarios",litrosNecesarios,"para recorrer km: ", km)
  
        #print("distancia real",distanciaReal)
        if self.motorArrancado==False or (self.motorArrancado== True and self.velocidadActual==0):
            print("No se puede recorrer distancia.")
        elif km < 0:
            print("Men, no se puede recorrer una distancia negativa")
        
        



        
    

    
    




