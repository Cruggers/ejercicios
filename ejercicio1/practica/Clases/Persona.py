# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:29:39 2022

@author: Emiliano
"""
from Clases.Email import email
import sys
     
class persona:
    nombre=""
    correo=""
    def __init__(self,xnom,id_,dom,tipo,contra):
        self.nombre=xnom
        self.correo=email(id_,dom,tipo,contra)
    def __init__(self):
        pass
    
    def Carga_usuario(self,xnombre):
        self.nombre=xnombre
        self.correo=email()
        self.correo.crearCuenta()
        return

    def mostrar_datos(self):
        print(self.nombre + ' ' + self.correo.getEmail())
        return
    
    def getNombre(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo
    
    def mostrarMEnsaje(self):
        print("Estimado "+self.nombre+"te enviaremos tus mensajes a la dirección "+self.correo.getEmail()+"\n")
        return