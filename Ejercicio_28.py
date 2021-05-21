# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:07:10 2021

@author: juanj
"""

def f_sumar(n1,n2,n3=0,n4=0,n5=0):
    suma=n1+n2+n3+n4+n5
    return suma

print("la suma de 5+6:",f_sumar(5,6))
print("La suma de 5+6+3:",f_sumar(5,6,3))
print("La suma de 1+1+1+1:",f_sumar(1,1,1,1))
print("La suma de 1+1+1+2+2:",f_sumar(1,1,1,2,2))