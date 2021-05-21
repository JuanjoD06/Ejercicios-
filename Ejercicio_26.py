# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:17:32 2021

@author: juanj
"""

def f_multiplicar(lista,numero):
    for i in range (len(lista)):
        multiplicacion=lista[i]*numero
        print(multiplicacion)
        
lista=[3,2,9,11,5]
print("Lista original",lista)
print ("Lista multiplicada por 3:")
f_multiplicar(lista,3)
