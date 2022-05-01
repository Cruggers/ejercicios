# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:20:25 2022

@author: Emiliano Emiliano  
"""

import sys, os, csv

from Clases.Persona import *


def buscar(lista,dato):
    if dato == lista:
        return True
    else:return False

if __name__ == "__main__":
    corte=True
    nuevo=persona()
    lista=[]
    while corte == True:
        print("================= Bienvenido =================\n")
        print("\n")
        print("Elija una opcion o precione '0' para terminar\n")
        print("1 - Nuevo usario\n")
        print("2 - Crear correo\n")
        print("3 - Cambiar contraseña\n")
        print("4 - leer fichero\n ")
        op = int(input("=> Ingrese opcion: "))
        if op==0:
            confirma=input("usted esta saliendo para confirmar precione Y para volver al menu precione N \n")
            if confirma=="y":
                print("hasta pronto")
                sys.exit()
        elif op==1:
            print("1 - Nuevo usario\n")
            nombre=input("Ingrese nombre de usuario: \n")
            nuevo.Carga_usuario(nombre)
            lista.append(nuevo)
        elif op==2:
            print("2 - Crear correo\n")
        elif op==3:
            print("3 - Cambiar contraseña\n")
            for i in range(len(lista)):
                if buscar(lista[i].getCorreo().getEmail(), dato=input("ingrese correo electronico:\n"))==True:
                    if buscar(lista[i].getCorreo().getContraseña(), dato=input("ingrese contraseña:\n"))==True:
                        lista[i].getCorreo().setCotraseña(input("ingrese nueva contraseña:\n"))
                        i=range(len(lista))
                    else:print("la contraseña ingresada no es valida\n")
                else:print("el usuario ingresado no existe\n")
        elif op==4:
            lineaCompleta = []
            archivo = open('usuarios.csv')
            reader = csv.reader(archivo,delimiter=';')
            for fila in reader:
                nuevo=persona(fila[0], fila[1], fila[2], fila[3], fila[4])
                lista.append(nuevo)
                nuevo.correo()
            archivo.close()
            
                        

            
            


            
        
        
        