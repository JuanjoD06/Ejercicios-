# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:38:15 2021

@author: juanj
"""

temperatura = float(input("Ingrese temperatura en °c:"))
var1 = 1.8 
var2 = 32

farenheit = temperatura * var1 + var2
kelvin = temperatura + 273.15

print("sus grados en °farenheit es:", farenheit)
print("sus grados en °kelvin es:",kelvin)

