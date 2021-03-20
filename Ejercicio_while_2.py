# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:22:09 2021

@author: juanj
"""
altos = 0
bajos = 0
x = 0
gastos = 0 
n = int(input("Ingrese numero de empleados:"))
while x < n:
    sueldo = int(input("Ingrese su sueldo"))
    if sueldo >= 300 :
         altos = altos + 1 
    else:
        bajos = bajos + 1
    gastos = gastos + sueldo
    x = x + 1    
print("Los trabajadores que ganan mas de 300 son:", altos)
print("Los trabajadores que ganan entre 100 y 300 son:", bajos)
print("Los gastos de la empresa son:",gastos)
    