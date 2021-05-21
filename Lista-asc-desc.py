# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:40:05 2021

@author: juanj
"""

# Métodos de ordenamiento

# Crear lista y darle valores

listaBase=[34,12,45,2,37,60,34,8]

print("Lista base: ",listaBase)
#Ordenar la lista con una función de python
listaBase.sort()
print("Lista base Ordenada Ascendente: ",listaBase)
  
#Ordenar la lista con una función de python
listaBase.sort(reverse=True)
print("Lista base Ordenada Descendente: ",listaBase)

#==========================================
#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp





unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)