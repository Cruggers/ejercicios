# -*- coding: utf-8 -*-
from Clases.viajero import Viajero_Frecuente

import csv
import sys

def Busca(lista,buscar):
    i=0
    while i<=len(lista) and lista[i].getNumeroViajero() != buscar:
        i=i+1
    if i != len(lista):
        return i
    else return None

if __name__ == "__main__":
    lista=list()
    #carga de fichero
    lineaCompleta = []
    archivo = open('Viajero.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        nuevo=Viajero_Frecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        lista.append(nuevo)
    archivo.close()
    parar=True
    while parar:
        print("a- Consultar Cantidad de Millas.\n")
        print("b- Acumular Millas.\n")
        print("c- Canjear Millas.\n")
        op=input("elija una opcion para terminar elija 0: \n")
        print("----------------------------------------\n")
        if op == 'a':
            new=int(input("ingrese numero de viajero:\n"))
            i=Busca(lista,new)
            print("----------------------------------------\n")
            print("numero de viajero: ",lista[i].getNumeroViajero(),"\n")
            print("----------------------------------------\n")
            print("cantidad de millas:",lista[i].CantidadTotaldeMillas(),"\n")
            print("---------------------------------------\n")
            input("precione una tecla para terminar:\n")
            print("----------------------------------------\n")
            
        elif op == 'b':
            new=int(input("ingrese numero de viajero:\n"))
            i=Busca(lista,new)
            lista[i].AcumularMillas(int(input("ingrese cantidad de millas nuevas:\n")))
            print("se a actualizada las millas de viajero\n")
            print("----------------------------------------\n")
            print("numero de viajero: ",lista[i].getNumeroViajero(),"\n")
            print("----------------------------------------\n")
            print("cantidad total: ",lista[i].CantidadTotaldeMillas(),"\n")
            print("----------------------------------------\n")
            input("precione una tecla para terminar:\n")
        elif op == 'c':
            new=int(input("ingrese numero de viajero:\n"))
            i=Busca(lista,new)
            total= lista[i].Canjear_millas(int(input("ingrese cantidad de millas a cambiar: \n")))
            if total == None:
                print("error en la operacion")
            else:
                print("----------------------------------------\n")
                print("numero de viajero: ",lista[i].getNumeroViajero(),"\n")
                print("----------------------------------------\n")
                print("cantidad total de millas acumuladas: ",total,"\n")
                print("----------------------------------------\n")
                input("precione una tecla para terminar:\n")
                
            
            
            
            
            
            
    
