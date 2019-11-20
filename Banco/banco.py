class Banco:
    def __init__(self,numero, titular):
        self.numero= numero
        self.titular= titular
        self.saldo = 0.0
        self.bloqueada= False
        pass
    def consultar(self):
        print("El saldo de la cuenta es ",self.saldo)
    def ingresarDinero(self, cantidad):
        if self.bloqueada== False:
            self.saldo+=cantidad
        else:
            print("No se puede ingresar dinero porque la cuenta está bloqueada")
    def retirarDinero(self, cantidad):
        if self.bloqueada== False:
            if cantidad> self.saldo:
             print("No tienes esa cantidad de dinero en tu cuenta.")
            else:
             self.saldo-=cantidad
        else:
            print("La cuenta está bloqueada: ")
    def cambioTitular(self, nuevoTitular):
        if self.bloqueada== False:
            if nuevoTitular != "":
                self.titular=nuevoTitular
            else:
                print("Nuevo titular no válido")
        else:
            print("No se puede cambiar de titular porque la cuenta está bloqueada")
    def bloquearCuenta(self):
        self.bloqueada= True
    def desbloquearCuenta(self):
        if self.bloqueada== True:
            self.bloqueada= False
    def imprimirDatos(self):
        print("El titular ",self.titular,"de la cuenta con el número ",self.numero,"tiene ",self.saldo,"saldo")

