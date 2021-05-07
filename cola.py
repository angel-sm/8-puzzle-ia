class Cola:
    def __init__(self, estado_inicial):
        self.cola = [estado_inicial]
        self.visitados = [estado_inicial]
    

    def insertarCola(self, estado):
        for visitado in self.visitados:
            if((estado == visitado).all()):
                return     

        for enCola in self.cola:
            if((estado == enCola).all()):
                return               
        
        self.cola.append(estado)
    
    def insertarVisitado(self, nodo):
        for visitado in self.visitados:
            if((nodo == visitado).all()):
                return         
        self.visitados.append(nodo)
    
    def tomarPrimerNodo(self):
        return self.cola.pop(0)

    def imprimirCola(self):
        print('\n COLA ')
        for item in range(len(self.cola)):
            print('\n',self.cola[item])
        print('>>>> \n ')

    def imprimirVisitados(self):
        print('\n visitados')
        for item in range(len(self.visitados)):
            print('\n V >>',self.visitados[item])
        print('>>>> \n ')

    def imprimirVisitadosTotal(self):
        print('Estados visitados', len(self.visitados))