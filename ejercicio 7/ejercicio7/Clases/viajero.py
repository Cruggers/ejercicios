import sys

class Viajero_Frecuente:
    __num_viajero: int
    __dni=""
    __nombre=""
    __apellido=""
    __millas_acum: int
    def __init__(self,xnum,xdni,xnom,xape,xmillas):
        self.__num_viajero=int(xnum)
        self.__dni=xdni
        self.__nombre=xnom
        self.__apellido=xape
        self.__millas_acum=int(xmillas)
    def CantidadTotaldeMillas(self):
        return self.__millas_acum
    def AcumularMillas(self,millas_ifrecoridas):
        self.__millas_acum=self.__millas_acum+millas_recoridas
        return self.__millas_acum
    def Canjear_millas(self,millas_caje):
        if millas_caje <= self.__millas_acum:
            self.__millas_acum=self.__millas_acum-millas_caje
            return self.__millas_acum
        else: return None
    def getNumeroViajero(self):
        return self.__num_viajero
    def getMillasAcumuladas(self):
        return self.__millas_acum
    def setMillasAcumuladas(self,valor):
        self.__millas_acum=valor
        
        
    #sobre carga de operadores
    
    
    def __add__ (self,suma):
        if type(suma) == int:
            return self.__millas_acum + suma
        def __radd__ (self,suma):
            if type(suma) == int:
                return self.__millas_acum + suma
    def __sub__ (self,valor):
        if type(valor) == int:
            return self.__millas_acum - valor
    def __rsub__(self,valor):
        if type(valor) == int:
            return self.__millas_acum - valor 
    def __gt__(self,compara):
        if type(self) == type(compara):
            return self.__millas_acum > compara.getMillasAcumuladas()
    def __eq__(self,valor):
        if type(valor) == int:
            return self.__millas_acum == valor
        
        
        