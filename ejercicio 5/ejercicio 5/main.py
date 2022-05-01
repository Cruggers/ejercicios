# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:16:49 2022

@author: Emiliano
"""

import sys, csv
from Clases.plan import PlanAhorro

def  Buscar(lista,busca):
    i=0
    while i <= len(lista) and busca != lista[i].getCodigoPlan():
        i=i+1
    if i != len(lista):
        return i
    else: return None
def BuscarPrcio (lista, busca):
    for i in range(len(lista)):
        if busca < lista[i].getValor():
            print("___________________________________________________________\n")
            print("codigo de plan:" , lista[i].getCodigoPlan() , "modelo:" , lista[i].getModelo() , "vercion:" , lista[i].getVercion(), "precio:" , lista[i].getValor())
            print("___________________________________________________________\n")
if __name__ == '__main__':
    lista=[]
    #carga punt 1
    lineaCompleta = []
    archivo = open('planes.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        nuevo=PlanAhorro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        lista.append(nuevo)
    archivo.close()
    #2
    parar = True
    while parar:
        print("___________________________________________________________\n")
        print("1 actualizar valor de vehiculo")
        print("2 buscar por valor")
        print("3 dinero adeudado para licitar")
        print("4 modificar cantidada de cuotas para licitar")
        op=input("ingrese una opcion para terminar 0:")
        if op == '1':
            i=0
            while i <= len(lista):
                print("___________________________________________________________\n")
                print("codigo de plan:" , lista[i].getCodigoPlan() , ", modelo:" , lista[i].getModelo() , ", vercion:" , lista[i].getVercion())
                print("___________________________________________________________\n")    
                nuevo=float(input("ingrese nuevo valor"))
                lista[i].Acutualiza_Valor(nuevo)
        elif op == '2':
            print("___________________________________________________________\n")
            BuscarPrcio(lista, float(input("ingrese valor:")))
            print("___________________________________________________________\n")
        elif op == '3':
            i=Buscar(lista,int(input("ingrese codigo de plan:")))
            if i != None:
                total=lista[i].ValorCuota() * lista[i].getLicitar()
                print("___________________________________________________________\n")
                print("Total a pagar:",total)
                print("___________________________________________________________\n")
            else:
                print("Error codigo no encontrado")
            
        elif op == '4':
            i=Buscar(lista,int(input("ingrese codigo de plan:")))
            if i != None:
                lista[i].setLicitar(int(input("ingrese nueva cantidad de cuotas:")))
            else:
                print("Error codigo no encontrado")
            
        elif op == '0':
            parar=False
        else: print("valor ingresado incorecto\n")
    
    
    