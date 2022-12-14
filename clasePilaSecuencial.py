import numpy as np

class Pila(object):
    __items = None
    __tope = None
    __cant = None
    
    def __init__(self, dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__tope = -1
        self.__cant = dimension
    
    def vacio(self):
        resultado = None
        if self.__tope == -1:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def insertar(self, elemento):
        assert isinstance(elemento,int)
        if self.__tope < self.__cant-1:
            self.__tope+=1
            self.__items[self.__tope]=elemento
            print('Elemento insertado: {}' .format(elemento))
        else:
            print('ERROR: pila llena!')
    
    def suprimir(self):
        valor = None
        if self.vacio():
            print('ERROR: pila vacia!')
            valor = 0
        else:
            valor = self.__items[self.__tope]   
            self.__tope-=1
        return valor
    
    
    def mostrar(self):
        if not self.vacio():
            while self.__tope >= 0:
                print('Elemento: {}' .format(self.suprimir()))
        else:
            print('ERROR: pila vacia!')
    
    

        
    
        
    
    
    