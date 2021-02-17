# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:25:49 2021

@author: juanj
"""

num1 = float(input("Ingrese un numero:"))
num2 = float(input("Ingrese un numero:"))

operacion = input("Ingrese la operacion que desea realizar:")

if operacion == "+":
    suma = num1 + num2
    print ("la suma es:", suma)

elif operacion == "-":
    resta = num1 - num2
    print ("la resta es:", resta)

elif operacion == "*":
    multiplicacion = num1 * num2
    print ("la multiplicacion es:", multiplicacion)

elif operacion == "/":
    division = num1 / num2
    print ("la division es:", division)
       
elif operacion == "*2":
    pot = num1 ** num2
    print ("la potencia es:",pot)

else: 
    print("error")
    
