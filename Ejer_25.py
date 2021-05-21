# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:08:08 2021

@author: juanj
"""

def f_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie
l1=int(input("Ingrese lado 1:"))
l2=int(input("Ingrese lado 2:"))
print("la superficie es ",f_superficie(l1,l2),"metros cuadrados")