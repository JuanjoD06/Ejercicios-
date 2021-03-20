# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:05:25 2021

@author: juanj
"""
#leer n generar numeros aleaotorios y calcular suma y promedio

#Librerias
import random 

#variables
cantidad_de_numeros = 0
cont_rep_while = 0 
prom = 0.0
suma = 0

#Variables segunda parte del ejercicio
acum_positivos = 0
acum_negativos = 0
cont_positivos = 0
cont_negativos = 0
prom_positivos = 0
prom_negativos = 0

#Variables tercera parte
mayor_pos = 0
mayor_neg = 0
menor_pos = 1000
menor_neg = 0


#entrada
cantidad_de_numeros = int(input("Cantidad de numeros:"))

#Procesos
while cont_rep_while<cantidad_de_numeros:
    numero=random.randint(0,100)
    suma=suma+numero
    #Segunda parte del ejercicio
    if numero>0: #calculo para numeros positivos
        print("Numero positivos:",numero)
        acum_positivos = acum_positivos + numero
        cont_positivos = cont_positivos + 1
        #Identificar el mayor positivo
        if numero>mayor_pos:
            mayor_pos = numero
            menor_neg = numero
        else:
            
    
    
    cont_rep_while=cont_rep_while+1
    #Fin del ciclo
prom=suma/cont_rep_while
print("Suma de numeros aleatorios:",suma)
print("Promedio de numeros aleatorios",prom)
print("Mayor numero positivo",mayor_pos)