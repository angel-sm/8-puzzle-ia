# [[8, 2, 3], [6, 0, 5], [4, 7, 1]]
# 1 2 3 
# 4 5 6 
# 7 8 0
import numpy as np

class Aestrella:

    cola = []
    estado_final = []
    visitados = []
    precola = []

    def __init__(self, estado_inicial, estado_final):
        self.cola = [estado_inicial]
        self.visitados = [estado_inicial]
        self.estado_final = estado_final

    def calcularHeuristica(self, estado):
        heuristica_calculada = 0
        totalRestaColumnas = 0
        totalRestaFilas = 0
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if estado[columna][fila] != self.estado_final[columna][fila]:
                    coordenadasEstadoActual = self.encontrarPosicion(
                        estado, estado[columna][fila])
                    coordenadasEstadoFinal = self.encontrarPosicion(
                        self.estado_final, estado[columna][fila])
                    
                    colX1 = coordenadasEstadoActual[0]
                    colX2 = coordenadasEstadoFinal[0]
                    
                    filaX1 = coordenadasEstadoActual[1]
                    filaX2 = coordenadasEstadoFinal[1]

                    if colX1 > colX2:
                      totalRestaColumnas = colX1 - colX2
                    else:
                      totalRestaColumnas = colX2 - colX1

                    if filaX1 > filaX2:
                      totalRestaFilas = filaX1 - filaX2
                    else:
                      totalRestaFilas = filaX2 - filaX1
                    
                    heuristica_calculada +=  totalRestaColumnas + totalRestaFilas
            
        return heuristica_calculada

    def preInsertarEnCola(self, estdo):

        if self.Existe(estdo, self.visitados):
          return
        if self.Existe(estdo, self.cola):
          return
        
        band = True
        i = 0
        if len(self.precola) == 0:
          self.precola.append(estdo)
        else:          
          while band:
            aux = self.precola[i]
            if(self.calcularHeuristica(aux) > self.calcularHeuristica(estdo)):
              self.precola[i] = estdo
              estdo = aux
              i = 0
            else:
              i += 1

            if i == len(self.precola):
              self.precola.append(estdo)
              band = False 

    def insertarCola(self):
        for estado in range(len(self.precola)):
          #print("\n Se agrego a la cola\n", self.precola[estado], "\n")
          self.cola.append(self.precola[estado])
        
        self.precola = []

    def Existe(self, estado, cola):
      for est in cola:
          if((np.array(estado) == np.array(est)).all()):
              return True

    def tomarPrimerNodo(self):
      return self.cola.pop(0)

    def insertarVisitado(self, estado):
        if self.Existe(estado, self.visitados):
            return
        self.visitados.append(estado)

    def encontrarPosicion(self, estado, numero):
        for columna in range(len(estado)):
            for fila in range(len(estado[columna])):
                if(estado[columna][fila] == numero):
                    return [columna, fila]

    def imprimirPreCola(self, step):
        print('\n imprimirPreCola')
        for item in range(len(self.precola)):
            print('\n',self.precola[item], self.calcularHeuristica(self.precola[item]), step)
        print('>>>> \n ')
    
    def imprimirCola(self, step):
      print('\n imprimirCola')
      for item in range(len(self.cola)):
          print('\n',self.cola[item], step)
      print('>>>> \n ')
    
    def imprimirVisitados(self, col, fil, step):
        print('\n imprimirVisitados')
        for item in range(len(self.visitados)):
            print('\n',np.array(self.visitados[item]).reshape(col, fil), step)
        print('>>>> \n ')
    
    def imprimirVisitadosTotal(self):
        print('Estados visitados', len(self.visitados))