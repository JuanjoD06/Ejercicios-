# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:24:57 2021

@author: juanj
"""

def f_mayor(lista):
    menor=0
    for i in range(1,len(lista)):
        if len(lista[i])>len(lista[menor]):
            menor=i
        return lista[menor]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",f_mayor(palabras))