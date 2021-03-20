# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:53:16 2021

@author: juanj
"""

#Leer una tabla de multiplicar e imprimir dicha tabla desde 1 hasta el 20 y sumar sus resultados
#Usar para la solución a ciclo for 
#Declarar variables
tabla = 0
multiplicador = 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1
#Leer el numero de la tabla para la cual vamos a realizar las operciones
tabla = int(input("Tabla :"))
#Leer el Multiplicador
multiplicador = int(input("Multiplicador :"))

#Inicio del ciclo repetitivo while
while(conRepCiclo < multiplicador):
    resultado = tabla * conRepCiclo
    print(tabla, "*", conRepCiclo, "=", resultado)
    sumaResultado = sumaResultado + resultado
#Incrementar la variable que controla el ciclo
    conRepCiclo = conRepCiclo + 1 
print("La suma es:",sumaResultado)