def newMatrix(f,c,n):
     matriz = []
     for i in range(f):
         a = [n]*c
         matriz.append(a)
     return matriz
newMatrix(2,5,2)
a = [[1,2,3],[7,8,9],[4,5,6]]
def show_matrix(M):
        """ Imprime los valores almacenados en la matriz """
        filas = len(M)
        columnas = len(M[0])
        for i in range(filas):
            for j in range(columnas):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(M[i][j]), sep=',', end='')
            print('|\n')

show_matrix(a)
