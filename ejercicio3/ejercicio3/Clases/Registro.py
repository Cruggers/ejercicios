# -*- coding: utf-8 -*-

class registro:
    __temperatura: int
    __humedad: int
    __precion: float
    def __init__(self,tem,hume,pre):
        self.__temperatura=int(tem)
        self.__humedad=int(hume)
        self.__precion=float(pre)
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPrecion(self):
        return self.__precion
    def setTemperatura(self,xt):
        self.__temperatura=xt
    def setHumedad(self,xh):
        self.__humedad=xh
    def setPrecion(self,xp):
        self.__precion=xp
    
    
    