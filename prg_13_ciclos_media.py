# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:31:19 2021

@author: juanj
"""
#Porgrama que lee N numeros enteros y calcula su promedio sale con un numero menor a 0

#Declarar variables
num = 0 #Variable que almacena los numeros que digita el usuario
suma = 0 #Variable que almacena la suma de los numeros positivos 
media = 0.0#Variable que almacena la media 
canele = 0#Variable que almacena la cantidad de numero digitados 

num = int(input("Numero:"))#Lectura del primer numero

while num > 0:
    suma = suma + num
    num = int(input("Numero:"))#Lectura de otros numeros
    canele = canele + 1
   #Termina el ciclo 
if canele !=0:    
    media = suma / canele
    print("la media es: ", media)    
else:
    print("No hay numero para calcular la media")