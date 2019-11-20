class Bombilla:
    #constructor de la bombilla
    def __init__(self):
        self.vecesEncendidas=0
        self.vecesApagadas=0
        self.estado= False
        pass
    #métodos propios
    def encender(self):
        self.vecesEncendidas+=1
        if self.vecesEncendidas<1001:
            self.estado= True
            #print("se ha encendido la bombilla")
    def apagar(self):
        self.vecesApagadas+=1
        self.estado= False
    def getVecesEncendidas(self):
        return self.vecesEncendidas
    def getVecesApagadas(self):
        return self.vecesApagadas
    def getEstado(self):
        return self.estado
 
        
