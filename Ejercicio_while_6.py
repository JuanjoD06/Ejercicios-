# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:50:24 2021

@author: juanj

"""
buenas = 0
malas = 0
x = 0


while x < 10:
    notas = float(input("Ingrese notas"))
    if notas >=7:
        buenas = buenas + 1
    else:
        malas = malas + 1
    x = x + 1    
     
    
print("Cantidad de notas buenas", buenas)
print("Cantidad de notas malas", malas)