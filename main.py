import numpy as np
from cola import Cola
from cuadro import Cuadro
from pila import Pila
from aestrella import Aestrella
import time

class MyClass:

    saludo = "Hola"

    def __init__(self):

        cuadro = Cuadro()

        print("Cuanta filas")
        filas = input()
        cuadro.setFilas(filas)
        print("Cuanta columnas")
        columnas = input()
        cuadro.setColumnas(columnas)
        valores=list(map(int, input("Inserta los numeros ").split()))

        self.generarEstadoFinal(valores, cuadro.getColumnas(), cuadro.getFilas(), cuadro)

        print("Cual metodo de bisqueda \n",
        "1: Ancho \n",
        "2: Profundidad \n",
        "3: A * \n")
        opcion = input()
        if int(opcion) == 1:
            self.BusquedaAncho(valores, cuadro)
        elif int(opcion) == 2:
            self.BusquedaProfundidad(valores, cuadro)
        else :
            self.BusquedAEstrella(valores, cuadro, cuadro.getEstadoFinal())
        
    def BusquedAEstrella(self, estadoActual, cuadro, estado_final):
        
        inicio = time.time()

        a_estrella = Aestrella(np.array(estadoActual).reshape(
            cuadro.getFilas(), cuadro.getColumnas()), estado_final)
        step = 0

        while(True):
            estadoActual = tuple(a_estrella.tomarPrimerNodo())
            if(self.validar(cuadro.getEstadoFinal(), estadoActual, cuadro.getColumnas(), cuadro.getFilas())):
                print("A *\n iteraciones: ", step)
                fin = time.time()
                print(fin-inicio)
                return
            arriba = cuadro.moverArriba(estadoActual)
            if type(arriba) != bool:
                a_estrella.preInsertarEnCola(arriba)

            derecha = cuadro.moverDerecha(estadoActual)
            if type(derecha) != bool:
                a_estrella.preInsertarEnCola(derecha)

            abajo = cuadro.moverAbajo(estadoActual)
            if type(abajo) != bool:
                a_estrella.preInsertarEnCola(abajo)

            izquierda = cuadro.moverIzquierda(estadoActual)
            if type(izquierda) != bool:
                a_estrella.preInsertarEnCola(izquierda)
            
            a_estrella.insertarVisitado(estadoActual)
            a_estrella.insertarCola()
            step += 1
        
    def BusquedaAncho(self, estadoActual, cuadro):

        inicio = time.time()

        step = 0

        cola = Cola(np.array(estadoActual).reshape(
            cuadro.getFilas(), cuadro.getColumnas()))

        while(True):
            estadoActual = tuple(cola.tomarPrimerNodo())

            if(self.validar(cuadro.getEstadoFinal(), estadoActual,  cuadro.getColumnas(), cuadro.getFilas())):
                print("Ancho\n iteraciones: ", step)
                fin = time.time()
                print(fin-inicio)
                return

            arriba = cuadro.moverArriba(estadoActual)
            if type(arriba) != bool:
                cola.insertarCola(arriba)

            derecha = cuadro.moverDerecha(estadoActual)
            if type(derecha) != bool:
                cola.insertarCola(derecha)

            abajo = cuadro.moverAbajo(estadoActual)
            if type(abajo) != bool:
                cola.insertarCola(abajo)

            izquierda = cuadro.moverIzquierda(estadoActual)
            if type(izquierda) != bool:
                cola.insertarCola(izquierda)

            cola.insertarVisitado(np.array(estadoActual).reshape(
                cuadro.getFilas(), cuadro.getColumnas()))
            
            step += 1

    def BusquedaProfundidad(self, estadoActual, cuadro):
        inicio = time.time()
        step = 0
        pila = Pila(np.array(estadoActual).reshape(cuadro.getFilas(), cuadro.getColumnas()))
        while(True):
            estadoActual = tuple(pila.tomarPrimerNodo())

            arriba = cuadro.moverArriba(estadoActual)
            if type(arriba) != bool:
                if(self.validar(cuadro.getEstadoFinal(), arriba,  cuadro.getColumnas(), cuadro.getFilas())):
                    print("Profundidad\n iteraciones: ", step)
                    fin = time.time()
                    print(fin-inicio)
                    return
                pila.insertarPila(arriba)

            derecha = cuadro.moverDerecha(estadoActual)
            if type(derecha) != bool:
                if(self.validar(cuadro.getEstadoFinal(), derecha,  cuadro.getColumnas(), cuadro.getFilas())):
                    print("Profundidad\n iteraciones: ", step)
                    fin = time.time()
                    print(fin-inicio)
                    return
                pila.insertarPila(derecha)

            abajo = cuadro.moverAbajo(estadoActual)
            if type(abajo) != bool:
                if(self.validar(cuadro.getEstadoFinal(), abajo,  cuadro.getColumnas(), cuadro.getFilas())):
                    print("Profundidad\n iteraciones: ", step)
                    fin = time.time()
                    print(fin-inicio)
                    return
                pila.insertarPila(abajo)

            izquierda = cuadro.moverIzquierda(estadoActual)
            if type(izquierda) != bool:
                if(self.validar(cuadro.getEstadoFinal(), izquierda,  cuadro.getColumnas(), cuadro.getFilas())):
                    print("Profundidad\n iteraciones: ", step)
                    fin = time.time()
                    print(fin-inicio)
                    return
                pila.insertarPila(izquierda)

            pila.insertarVisitado(np.array(estadoActual).reshape(
                cuadro.getFilas(), cuadro.getColumnas()))
            step += 1


    def validar(self, final, estadoActual, col, fil):
        if((np.array(final) == np.array(estadoActual)).all()):
            print('\n>>FIN>> \n')
            print(np.array(estadoActual).reshape(col, fil))
            print('\n>>FIN>> \n')
            return True

    def generarEstadoFinal(self, valores, filas, columnas, cuadro):
        valores_ordenados = np.sort(valores)
        lista_valors = list(valores_ordenados)
        num_cero = lista_valors.pop(0)
        lista_valors.append(num_cero)
        estado_final = np.array(lista_valors).reshape(filas, columnas)
        cuadro.setEstadoFinal(tuple(map(tuple, estado_final)))


MyClass()
