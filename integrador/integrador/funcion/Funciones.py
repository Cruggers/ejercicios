# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:00:45 2022

@author: Emiliano
"""
import sys
import csv
from datetime import datetime
from Clases.camas import Cama
from Clases.medicamento import Medicamento

def cargaCama():
    lista=[]
    lineaCompleta = []
    archivo = open('camas.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        nuevo=Cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
        i=int(fila[0])-1
        lista.append(nuevo)
    archivo.close()
    return lista
def cargaMedicamento():
    lista=[]
    lineaCompleta = []
    archivo = open('medicamentos.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        nuevo=Medicamento(int(fila[0]),int(fila[1]), fila[2], fila[3], fila[4], fila[5], float(fila[6]))
        lista.append(nuevo)
    archivo.close()
    return lista
def buscaNombre(lista,buscar):
    
    for i in range(len(lista)):
        if lista[i].getNombre()==buscar:
            return i
    return None

def listarAlta(medi,cama):
    i=buscaNombre(cama, input("\n ingrese nombre y apellido a buscar "))
    if i != None:
        cama[i].setAlta(datetime.today().strftime('%d-%m-%Y'))
        cama[i].mostrardatos()
        print("Medicamento/monodroga     Presentacion     Cantidad     Precio")
        total=0
        for lista in medi:
            if lista.getIdcama() == i+1:
                lista.mostrar()
                total=lista.getPrecio()+total
        print("Total adeudado:                                       ",total)
    else: print("el nombre no es correcto")

def listarpaciente(cama):
    for mostrar in cama:
       if mostrar.getEstado()==True:
           print("paciente:",mostrar.getNombre()," diagnostico:",mostrar.getDiagnostico())
            
    
    



