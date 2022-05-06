# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:34:12 2022

@author: Emiliano
"""
import sys
class Conjunto:
    __conjunto:list 
    def __init__(self,lista):
        self.__conjunto=lista
    def getConjunto(self):
        return self.__conjunto
    def __add__(self,conjunto):
        if type(self)==type(conjunto):
            a=set(self.__conjunto)
            b=set(conjunto.getConjunto())
            return a.union(b)
    def __sub__(self,conjunto):
        if type(self)==type(conjunto):
            a=set(self.__conjunto)
            b=set(conjunto.getConjunto())
            return a.difference(b)
    def __eq__(self, conjunto):
        if type(self) == type(conjunto):
            a=set(self.__conjunto)
            b=set(conjunto.getConjunto())
            return a==b

                    
                
        
                
                            