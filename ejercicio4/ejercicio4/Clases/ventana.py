# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:04:08 2022

@author: Emiliano
"""

import sys

class Ventana:
A    __titulo=""
    __superior_x:int
    __superior_y:int
    __inferior_x:int
    __inferior_y:int
    
    def __init__(self,titulo,sx=0,sy=0,ix=500,iy=500):
        self.__titulo=titulo
        self.__superior_x=sx
        self.__superior_y=sy
        self.__inferior_x=ix
        self.__inferior_y=iy
        
    def mostrar(self):
        print("           titulo:",self.__titulo)
        print("(",self.__superior_x,",",self.__superior_y,")")
        print("      ________________________")
        print("     │                        │")
        print("     │                        │")
        print("     │                        │")
        print("     │                        │")
        print("     │                        │")
        print("     │                        │")
        print("      ────────────────────────")
        print("                                (",self.__inferior_x,",",self.__inferior_y,")")

    def moverDerecha(self,valor=1):
        sx = valor + self.__superior_x
        ix = valor + self.__inferior_x
        if self.verificaRango(ix) != None and self.Verifica_x(sx) == True:
            self.__superior_x = sx
            self.__inferior_x = ix
        else: print("\n rango de desplazamiento invalido \n")
        
    def moverIzquierda(self,valor=1):
        sx = self.__superior_x - valor
        ix = self.__inferior_x - valor
        if self.verificaRango(sx) != None and self.Verifica_x(sx) == True:
            self.__superior_x = sx
            self.__inferior_x = ix
        else: print("\n rango de desplazamiento invalido \n")
        
    def bajar(self,valor=1):
        sy = valor - self.__superior_y
        iy = valor - self.__inferior_y
        print(iy)
        if self.verificaRango(iy) != None and self.Verifica_y(sy) == True:
            self.__superior_y = sy
            self.__inferior_y = iy
        else: print("\n rango de desplazamiento invalido \n")
        
    def subir(self,valor=1):
        sy = self.__superior_y + valor
        iy = self.__inferior_y + valor
        if self.verificaRango(sy) != None and self.Verifica_y(sy) == True:
            self.__superior_y = sy
            self.__inferior_y = iy
        else: print("\n rango de desplazamiento invalido \n")
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__inferior_y
    
    def ancho(self):
        return self.__inferior_x
    
    def verificaRango(self,verificar):
        if verificar >= 0 and verificar <= 500:
            return verificar
        else:
            print("error de rango")
            return None
        
    def Verifica_x (self,x):
        if x < self.__inferior_x:
            return True
        else: return False
        
    def Verifica_y (self,y):
            if y < self.__inferior_y:
                return True
            else: return False

    