# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:36:36 2021

@author: juanj
"""

tabla = 0
multiplicador = 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1
#Leer el numero de la tabla para la cual vamos a realizar las operciones
tabla = int(input("Tabla :"))
#Leer el Multiplicador
multiplicador = int(input("Multiplicador :"))

for conRepCiclo in range (multiplicador + 1):
    resultado = tabla * conRepCiclo
    print(tabla, "*", conRepCiclo, "=", resultado)
    sumaResultado = sumaResultado + resultado
print("La suma es:",sumaResultado)