# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:00:59 2021

@author: juanj
"""

def f_retornar(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    return promedio

num1=int(input("Ingrese primer numero"))
num2=int(input("Ingrese segundo numero"))
num3=int(input("Ingrese tercer numero"))
print("valor de los numeros ingresados",f_retornar(num1,num2,num3))

