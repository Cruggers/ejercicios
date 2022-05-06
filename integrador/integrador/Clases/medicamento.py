# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:33:43 2022

@author: Emiliano
"""

import sys

class Medicamento:
    
    __idCama:int 
    __idMedicamento:int 
    __nombre_comercial=""
    __monodroga=""
    __presentacion=""
    __cantidad_aplicada=""
    __precio:float
    
    def __init__(self,idc,idme,nomc,mono,pres,can,pre):
        self.__idCama=idc
        self.__idMedicamento=idme
        self.__nombre_comercial=nomc
        self.__monodroga=mono
        self.__presentacion=pres
        self.__cantidad_aplicada=can
        self.__precio=pre
        
    def getIdcama(self):
        return self.__idCama
    
    def getPrecio(self):
        return self.__precio
    
    def mostrar(self):
        print(self.__nombre_comercial,"",self.__monodroga,"    ",self.__presentacion,"    ",self.__cantidad_aplicada,"       ",self.__precio)