# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:28:28 2021

@author: juanj
"""

def f_ingreso():
     num1=int(input("Ingrese un entero"))
     num2=int(input("Ingrese un entero"))
     num3=int(input("Ingrese un entero"))
     if num1<num2 and num1<num3:
         print(num1)
     else:
         if num2<num3 and num2<num1:
             print(num2)
         else:
            print(num3)

f_ingreso()
f_ingreso()