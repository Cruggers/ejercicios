# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:23:35 2022

@author: Emiliano
"""

import sys
import csv

from Clases.Registro import registro

def Busca_mayor (lista):
    mayor=registro(25, 50, 50)
    humedad=[]
    precion=[]
    temperatura=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].getHumedad() >= mayor.getHumedad():
                humedad=[i+1,j,mayor.getHumedad()]
                mayor.setHumedad(lista[i][j].getHumedad())
            if lista[i][j].getPrecion() >= mayor.getPrecion():
                precion=[i+1,j,mayor.getPrecion()]
                mayor.setPrecion(lista[i][j].getPrecion())
            if  lista[i][j].getTemperatura() >= mayor.getTemperatura():
                temperatura=[i+1,j,mayor.getTemperatura()]
                mayor.setTemperatura(lista[i][j].getTemperatura())
    print("el dia de mayor temperuatura fue:",temperatura[0]," a las:",temperatura[1]," y fue de:",temperatura[2],"C°\n")
    print("el dia de mayor humedad fue:",humedad[0]," a las:",humedad[1]," y fue de:",humedad[2],"%\n")
    print("el dia de mayor precion fue:",precion[0]," a las:",precion[1]," y fue de:",precion[2],"\n")      
        
def Busca_menor (lista):
    mayor=registro(50, 100, 100)
    humedad=[]
    precion=[]
    temperatura=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].getHumedad() <= mayor.getHumedad():
                humedad=[i+1,j,mayor.getHumedad()]
                mayor.setHumedad(lista[i][j].getHumedad())
            if lista[i][j].getPrecion() <= mayor.getPrecion():
                precion=[i+1,j,mayor.getPrecion()]
                mayor.setPrecion(lista[i][j].getPrecion())
            if  lista[i][j].getTemperatura() <= mayor.getTemperatura():
                temperatura=[i+1,j,mayor.getTemperatura()]
                mayor.setTemperatura(lista[i][j].getTemperatura())
    print("el dia de menor temperuatura fue:",temperatura[0]," a las:",temperatura[1]," y fue de:",temperatura[2],"C°\n")
    print("el dia de menor humedad fue:",humedad[0]," a las:",humedad[1]," y fue de:",humedad[2],"%\n")
    print("el dia de menor precion fue:",precion[0]," a las:",precion[1]," y fue de:",precion[2],"\n")                            

def Promedio (lista):
    acum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            acum[j]=acum[j]+lista[i][j].getTemperatura()
    dias=len(lista)
    print("---------------------------------------------------------\n")
    print("promedio de temperatura por hora")
    for i in range(25):
        prom=acum[i]/dias
        print("promedio de temperatura para la hora:",i,":00 es ",prom,"\n")
    print("---------------------------------------------------------\n")
    input("Precione una tecla para continuar:")
     
if __name__ == "__main__":
    lista=[[],[]]
    #carga de fichero
    lineaCompleta = []
    archivo = open('Datos.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        nuevo=registro(fila[2], fila[3], fila[4])
        i=int(fila[0])-1
        lista[i].append(nuevo)
    archivo.close()
    #cierra fichero
    para=True
    while para:
        print("---------------------------------------------------------\n")
        print("1-   Mostrar para cada variable el día y hora de menor y mayor valor.\n")
        print("2- Indicar la temperatura promedio mensual por cada hora.\n")
        print("3-  Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.")
        op=int(input("ingrese opcion o precione 0 para ternimar :\n"))
        if op == 1:
            print("---------------------------------------------------------\n")
            Busca_mayor(lista)
            print("---------------------------------------------------------\n")
            Busca_menor(lista)
            print("---------------------------------------------------------\n")
            input("Precione una tecla para continuar:")
        elif op == 2:
            Promedio(lista)
        elif op ==3:
            dia=int(input("ingrese dias:"))
            print("---------------------------------------------------------\n")
            print("hora---------temperatura----------humedad---------precion\n")
            for i in range(len(lista[dia-1])):
                print(i,": 00 -------",lista[dia][i].getTemperatura(),"C° -------",lista[dia][i].getHumedad(),"% -------",lista[dia][i].getPrecion(),"\n")
            print("---------------------------------------------------------\n")
            input("Precione una tecla para continuar:")
        elif op == 0:
            sys.exit()
        else: print("la opcion ingresada es incorecta")
            

    
    
    
    
    