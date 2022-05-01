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
    else: return None

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
        print("a- listar viajeros con mayor cantidad de millas.\n")
        print("b- Acumular Millas.\n")
        print("c- Canjear Millas.\n")
        op=input("elija una opcion para terminar elija 0: \n")
        print("----------------------------------------\n")
        if op == 'a':
            maximo=0
            ant=0
            for i in range(len(lista)):
                if i+1 != len(lista): 
                    if lista[i]<lista[i+1]:
                        maximo=lista[i].getMillasAcumuladas()
                else: 
                    if lista[i].getMillasAcumuladas() > maximo:
                        ant=maximo
                        maximo=lista[i].getMillasAcumuladas()
            print(maximo,ant)
        elif op == 'b':
            new=int(input("ingrese numero de viajero:\n"))
            i=Busca(lista,new)
            valor=int(input("ingrese millas:"))
            #operador __add__
            lista[i].setMillasAcumuladas(lista[i]+valor)
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
            total=lista[i]-int(input("ingrese cantidad de millas:"))
            if total != 0:
                lista[i].setMillasAcumuladas(total)
                print("----------------------------------------\n")
                print("numero de viajero: ",lista[i].getNumeroViajero(),"\n")
                print("----------------------------------------\n")
                print("cantidad total de millas acumuladas: ",lista[i].getMillasAcumuladas(),"\n")
                print("----------------------------------------\n")
                input("precione una tecla para terminar:\n")
            else:
                print("----------------------------------------\n")
                print("Millas insuficientes")
                print("----------------------------------------\n")
                input("precione una tecla para terminar:\n")
                
        elif op == 'd':
            print(lista[1]+10)
            print(lista[1]-20)
            print(lista[0]>lista[1])
        
            
            
            
            
            
            
    
