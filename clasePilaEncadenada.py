from pickle import NONE
from claseNodo import Nodo

class Pila(object):
    __tope = None
    __cant = None
    
    def __init__(self):
        self.__tope = None
        self.__cant = 0
    
    def vacia(self):
        valor = None
        if self.__cant == 0:
            valor = True
        else:
            valor = False
        return valor
    
    def insertar(self, elemento):
        assert isinstance(elemento,int)
        unNodo = Nodo(elemento)
        unNodo.setSiguiente(self.__tope)
        self.__tope = unNodo
        self.__cant+=1
        valor = unNodo.getDato()
        return valor
    
    def suprimir(self):
        valor = None
        if self.vacia():
            print('ERROR: Pila vacia')
            valor = 0
        else:
            valor = self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__cant-=1
        return valor
    def getCantidad(self):
        return self.__cant
    
if __name__ == '__main__':
    x1 = 2
    x2 = 2
    print(x1%x2)
            
            
        