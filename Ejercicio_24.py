# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:54:35 2021

@author: juanj
"""
def f_cantidad_vocales(cadena):
    cant=0
    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u" :
            cant=cant+1
            print("cantidad de vocales de la palabra ",cadena, "es",cant)
    
f_cantidad_vocales("google")
