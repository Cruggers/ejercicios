# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:31:42 2022

@author: Emiliano
"""
import sys,csv
from funcion.Funciones import *

if __name__ == "__main__":
    medicina=list()
    camas=list()
    medicina=cargaMedicamento()
    camas=cargaCama()
    print("_________________________________________")
    print("__________________menu___________________")
    print("_________________________________________")
    print("1. dar alta a paciente")
    print("2 listar pacientes con diagnostico")
    print("0 para ternimar")
    op=int(input("elija su opcion:"))
    ban=True
    while ban:
        if op== 1:
            listarAlta(medicina, camas)
        elif op == 2:
            listarpaciente(camas)
        elif op == 0:
            sys.exit("hasta luego")