# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:53:24 2021

@author: juanj
"""

peso = float(input("ingrese su peso en (kg):"))

estatura = float(input("ingrese su estatura en (m):"))

masacorporal= peso/estatura**2

indice = (masacorporal)

print ("su masa corporal es:", indice)