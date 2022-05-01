# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:29:59 2022

@author: Emiliano
"""

class email:
    __id_cuenta = ""
    __dominio = ""
    __tipo_de_dominio = ""
    __contraseña = ""
    def __init__ (self,id_,dom,tipo,contra):
        self.id_cuenta=id_
        self.dominio=dom
        self.tipo_de_dominio=tipo
        self.contraseña=contra
        return
    
    def __init__(self):
        pass
    
    def getEmail(self):
        mail=self.id_cuenta+"@"+self.dominio+"."+self.tipo_de_dominio
        return mail
    
    def getDominio(self):
        return self.tipo_de_dominio
    
    def crearCuenta(self):
        nuevo=input("ingrese nuevo correo \n")
        self.setCuenta(nuevo)
        self.contraseña=input("ingrese contraseña \n")
        return
    
    def setCuenta(self, correo):
        correo=correo.split('@')
        self.id_cuenta=correo[0]
        correo=correo[1].split('.')
        self.dominio=correo[0]
        self.tipo_de_dominio=correo[1]
        return
    def getContraseña(self):
        return self.contraseña
    def setCotraseña(self,new):
        self.contraseña=new