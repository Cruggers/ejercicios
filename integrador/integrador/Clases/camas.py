# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:33:33 2022

@author: Emiliano
"""

import sys

class Cama:
    __idCama:int 
    __habitacion:int 
    __estado:bool
    __nombre_apellido=""
    __diagnostico=""
    __fecha_internacion=""
    __fecha_alta=""
    def __init__(self,xide,xhabitacion,xestado,xnombre,xdiagnostico,xfecha,xalta):
        self.__idCama=int(xide)
        self.__habitacion=int(xhabitacion)
        self.__estado=bool(xestado)
        self.__nombre_apellido=xnombre
        self.__diagnostico=xdiagnostico
        self.__fecha_internacion=xfecha
        self.__fecha_alta=xalta
        
    def getNombre(self):
        return self.__nombre_apellido
    def setAlta(self,fecha):
        self.__fecha_alta=fecha
    def mostrardatos(self):
        print("Paciente: ",self.__nombre_apellido," Cama: ",self.__idCama, "Habitación: ",self.__habitacion)
        print("Diagnóstico: ",self.__diagnostico, "Fecha de internación: ",self.__fecha_internacion)
        print("Fecha de Alta: ",self.__fecha_alta)
    def getEstado(self):
        return self.__estado
    def getDiagnostico(self):
        return self.__diagnostico
        