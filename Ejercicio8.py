# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:04:40 2021

@author: juanj
"""

masa = float(input("Ingrese la masa (kg):"))
coeficiente_r = float(input("Ingrese la fuerza de rozamiento:"))
newton = masa * 10
coeficiente = coeficiente_r * newton
print ("Su fuerza de friccion es:", coeficiente)
