# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:15:01 2021

@author: juanj
"""

print("ingrese 3 nu#meros enteros diferenetes") #mensaje para el usuario 
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))#se le pide al usuario elegir la opcion que necesite 
a = int(input("ingrese el numero a"))#Se le pide un numero
b = int(input("ingrese el numero b"))#Se le pide un numero
c = int(input("ingrese el numero c"))#Se le pide un numero

if (e == 1): #Si la variable "e" es = a "1" (opcion 1: de mayor a menor)  
    if (a > b): # si a es mayor a b
        if (a > c):#si a es mayor a c 
            if(b > c):#si b es mayor a c
               print(a, b, c) #mensaje en pantalla muestra los # en este órden 
            else:
               print(a, c, b)#en otro caso (si b es menor que c) seguiria este órden 
    if (c > a): #si c es mayor a a
        if (c > b):#si c es mayor a b
            if(b > a):#si b es mayor a a 
               print(c, b, a)#mensaje en pantalla muestra los # en este órden 
            else:
               print(c, a, b)#en otro caso (si b es menor que a) seguiria este órden
    if (b > a):#si b es mayor a a 
        if (b > c):#si b es mayor a c 
            if(a > c):#si a es mayor a c 
               print(b, a, c)#seguira este órden 
            else:
               print(b, c, a)#en otro caso (si a es menor que c) seguiria este órden

 
if (e == 2):#Si la variable "e" es = a "2" (opcion 2: de menor a mayor) 
    if (a < b):#si a es menor que b
        if (a < c):#si a es menor que c 
            if(b < c):#si b es menor que c
               print(a, b, c)#seguira este órden
            else:
               print(a, c, b)#en otro caso (si c es menor que b) seguiria este órden
    if (c < a):#si c es menor que a
        if (c < b):#si c es menor que b 
            if(b < a):#si b es menor que a 
               print(c, b, a)#seguira este órden
            else:
               print(c, a, b)#en otro caso (si a es menor que b) seguiria este órden
    if (b < a):#si b es menor que a 
        if (b < c):#si b es menor que c
            if(a < c):#si a es menor que c
               print(b, a, c)#seguira este órden 
            else:
               print(b, c, a)#en otro caso (si c es menor que a) seguiria este órden

if (a == b):# si "a" es igual a "b" 
    print("b y a son iguales")#imprime en pantalla que son iguales 
    if (a == c):#si "a" es igual a "c"
        print("a y c son iguales")#imprime en pantalla que son iguales 
        if(b == c):#si "b" es igual a "c"
           print(" b y c con iguales")#imprime en pantalla que son iguales 
           if(a == b == c):#si "a" "b" y "c" son iguales
              print("todos son iguales")#imprime en pantalla que son iguales 