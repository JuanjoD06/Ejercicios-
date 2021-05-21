# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:48:12 2021

@author: juanj
"""

def f_ordenar(n1,n2,n3):
    if n1<n2 and n1<n3:
        if n2<n3:
            print(n1.n2,n3)
        else:
            print(n1,n3,n2)
    else:   
        if n2<n3:
            if n1<n3:
                print(n2,n1,n3)
        else:
            if n1<n2:
                print(n3,n1,n2)
            else:
                print(n3,n2,n3)

def f_cargar():
    num1=int(input("ingrese primer valor"))
    num2=int(input("ingrese segundo valor"))
    num3=int(input("ingrese tercer valor"))
    f_ordenar(num1,num2,num3)

f_cargar()