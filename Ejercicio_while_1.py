# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:47:32 2021

@author: juanj
"""
suma = 0
x= 1
n = int(input("Ingrese numero de personas"))

while x <= n:
     altura = float(input("Ingrese altura"))
     suma = suma + altura
     x = x+1
promedio = suma / n
print ("Altura promedio:", promedio)
        