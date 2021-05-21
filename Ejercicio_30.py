# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:17:55 2021

@author: juanj
"""

def f_cantidad_mayores18(edad,*edades):
    cant=0
    if edad>=18:
        cant=cant+1
    for i in range(len(edades)):
        if edades[i]>=18:
            cant=cant+1
    return cant

print("Cantidad de personas mayores a 18años son:",f_cantidad_mayores18(23,26,35,99))
