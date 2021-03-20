# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:25:49 2021

@author: juanj
"""

fact_M=1
fact_N=1
fact_MN=1

#calculo de la combinatoria de dos numeros
#entradas 
ve_M=int(input("Digite M"))
ve_N=int(input("Digite N"))
for i in range(1,ve_M+1,1):
    fact_M=fact_M*i
#calcular factorial de n
vp_conRepWhile=1
while(vp_conRepWhile<=ve_N):
    fact_N=fact_N*vp_conRepWhile
    vp_conRepWhile=vp_conRepWhile+1

#calcular el factorial de m-n
vp_difMN=ve_M-ve_N 
for j in range(1,vp_difMN+1,1):
    fact_MN=fact_MN*j
    
#calcular combinatoria

vp_com=fact_M/(fact_N*fact_MN)

#Salidas
print("Factorial de M:",fact_M)
print("Factorial de N:",fact_N)
print("Factorial de M-N:",fact_MN)
print("combinatoria de MN:",vp_com)