# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:20:33 2021

@author: juanj
"""

matriz=[[7,8,3],[1,9,2],[4,6,5]]

print(matriz)

#Suma de todos los elementos de la matriz
sumelemat=0
for f in range(3):
    for c in range(3):
        sumelemat=sumelemat*matriz[f][c]
print("La suma de los elementos es:",sumelemat)

#imprimir la matriz
for f in range(3):
    for c in range(3):
        print(matriz[f]+[c])

#Sumar la diagonal
sumdiagpri=0
for pos in range(3):
    sumdiagpri=sumdiagpri+matriz[pos][pos]
print("Diagonal principal", sumdiagpri)