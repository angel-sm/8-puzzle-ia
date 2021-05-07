import numpy as np

class Cuadro:
    filas= 3
    columnas = 3
    estado_final = []

    def getEstadoFinal(self):
        return self.estado_final
    
    def setEstadoFinal(self, estado_final):
        self.estado_final = estado_final
    
    def getFilas(self):
        return int(self.filas)
    
    def setFilas(self, filas):
        self.filas = filas

    def getColumnas(self):
        return int(self.columnas)
    
    def setColumnas(self, columnas):
        self.columnas = columnas


    def moverArriba(self, estado):
        estado = np.array(estado).reshape(self.getFilas(), self.getColumnas())
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if(estado[columna][fila] == 0):
                    if(not columna-1 < 0):
                        valorAnterior = estado[columna-1][fila]
                        estado[columna-1][fila] = 0
                        estado[columna][fila] = valorAnterior
                        return estado
        return False

    def moverAbajo(self, estado):
        estado = np.array(estado).reshape(self.getFilas(), self.getColumnas())
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if(estado[columna][fila] == 0):
                    if(columna+1 < self.getColumnas()):
                        valorAnterior = estado[columna+1][fila]
                        estado[columna+1][fila] = 0
                        estado[columna][fila] = valorAnterior
                        return estado

        return False

    def moverDerecha(self, estado):
        estado = np.array(estado).reshape(self.getFilas(), self.getColumnas())
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if(estado[columna][fila] == 0):
                    if(fila+1 < self.getFilas()):
                        valorAnterior = estado[columna][fila+1]
                        estado[columna][fila+1] = 0
                        estado[columna][fila] = valorAnterior
                        return estado
        return False 
    
    def moverIzquierda(self, estado):
        estado = np.array(estado).reshape(self.getFilas(), self.getColumnas())
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if(estado[columna][fila] == 0):
                    if(not fila-1 < 0):
                        valorAnterior = estado[columna][fila-1]
                        estado[columna][fila-1] = 0
                        estado[columna][fila] = valorAnterior
                        return estado

        return False 