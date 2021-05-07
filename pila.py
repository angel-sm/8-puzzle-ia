class Pila:
    def __init__(self, estado_inicial):
        self.pila = [estado_inicial]
        self.visitados = [estado_inicial]
    
    def insertarPila(self, estado):
        for visitado in self.visitados:
            if((estado == visitado).all()):
                return     

        for enPila in self.pila:
            if((estado == enPila).all()):
                return               
    
        self.pila.append(estado)
    
    def insertarVisitado(self, estado):
        for visitado in self.visitados:
            if((estado == visitado).all()):
                return         
        self.visitados.append(estado)
    
    def tomarPrimerNodo(self):
        return self.pila.pop(len(self.pila) - 1)

    def imprimirPila(self):
        print('\n PILA ')
        for item in range(len(self.pila)):
            print('\n',self.pila[item], 'pos >',item)
        print('>>>> \n ')

    def imprimirVisitados(self):
        print('\n visitados')
        for item in range(len(self.visitados)):
            print('\n V >>',self.visitados[item], 'pos >',item)
        print('>>>> \n ')
    
    def imprimirVisitadosTotal(self):
        print('Estados visitados', len(self.visitados))
