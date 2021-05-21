# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:13:00 2021

@author: juanj
"""

def f_tabla(numero,terminos=11):
    for i in range (terminos):
        va=i*numero
        print(va,",",sep="",end="")
    print()
      
print("tabla del 4")
f_tabla(4)
print("Tabla del 4 con 5 terminos")
f_tabla(3,5) 