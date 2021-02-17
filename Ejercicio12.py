# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:27:07 2021

@author: juanj
"""

nombre = input("Ingrese su nombre:")

horas = float(int(input("Ingrese horas trabajadas:")))
hora = float(int(input("Ingrese valor de hora ($):")))

d = 0.2
sueldo = horas * hora
descuento = sueldo * 0.7

print("nombre:",nombre)

if descuento < 300:
    desc = descuento + d
    print("Su sueldo es:", desc)

elif descuento > 300:
    print("Su sueldo es:", descuento)
    
else: 
    print("error")
     