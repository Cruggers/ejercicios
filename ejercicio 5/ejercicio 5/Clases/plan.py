# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:17:07 2022

@author: Emiliano
"""
import sys

class PlanAhorro:
    __codigo_de_plan:int
    __modelo=""
    __vercion=""
    __valor:float
    __cuotas:int
    __licitar:int
    def __init__(self,xco,xm,xver,xva,xcuo,xli):
        self.__codigo_de_plan=int(xco)
        self.__modelo=xm
        self.__vercion=xver
        self.__valor=float(xva)
        self.__cuotas=int(xcuo)
        self.__licitar=int(xli)
    def Acutualiza_Valor(self,valor):
        self.__valor=valor
    def ValorCuota(self):
        total = (self.__valor / self.__cuotas) + (self.__valor * 0.10)
        return total
    def getCodigoPlan(self):
        return self.__codigo_de_plan
    def getModelo(self):
        return self.__modelo
    def getVercion(self):
        return self.__vercion
    def getValor(self):
        return self.__valor
    def getLicitar(self):
        return self.__licitar
    def setLicitar(self, valor):
        self.__licitar=valor
    
        
        
        
        
        