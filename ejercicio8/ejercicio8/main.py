# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:33:30 2022

@author: Emiliano
"""
import sys

from Clases.conjunto import Conjunto

if __name__ == "__main__":

    a=[1,2,3,4]
    b=[3,6,9]
    A=Conjunto(a)
    B=Conjunto(b)
    print(A+B)
    print(A-B)
    if A==B:
        print("los conjuntos son iguales")
    else:print("los conjuntos no son iguales")
