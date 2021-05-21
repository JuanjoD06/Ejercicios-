# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:39:15 2021

@author: juanj
"""
#declarar el valor lista 
Listanotas=[]
Listaganadas=[]
Listaperdidas=[]
sumanotas=0.0
#Asignar valores a la lista con ciclo
for posLista in range (5):
    #leer desde teclado la nota
    notaEst=float(input("Digite Nota:"))
    #Almacenamos la escalar en arreglo 
    Listanotas.append(notaEst)
    #sumamos notas
    sumanotas=(sumanotas+notaEst)
    #las notas sumadas se dividen entre las notas que hay 
    prom=sumanotas/5
    if notaEst > 3.0:
        Listaganadas.append(notaEst)
    elif notaEst < 3.0: 
        Listaperdidas.append(notaEst)

print("notas:",Listanotas)   
print("Las notas ganadas son:",Listaganadas)
print("La notas perdidas son:",Listaperdidas)
print("El promedio es:",prom)



