# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:08:16 2021

@author: juanj
"""
cantEst=int(input("Cantidad de estudiantes:"))
#Inicializar la variable que inicia el ciclo 
conRep=0
while (conRep < cantEst):
#Instrucciones a repetir
    nomEst = input("Nombre del estudiante:")
    notUnoEst = float(input("parcial uno:")) 
    notDosEst = float(input("parcial Dos:")) 
    notTresEst = float(input("parcial tres:")) 
    #calculos
    notDefEst = (notUnoEst+notDosEst+notTresEst)/3

    print(f"La nota definitiva es: {notDefEst:.2f}")
    conRep = conRep+1
    
