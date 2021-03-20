# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:20:41 2021

@author: juanj
"""

import math 

def f_titulo():
    print("Calculo de la hipotenusa de un triangulo rectangulo")

def f_calcularhipotenusa():
    #variables
    ve_catetouno = 0.0
    ve_catetodos = 0.0
    vps_radicando = 0.0
    vps_hipotenusa = 0.0
    #vps_perimetro = 0.0
    #entradas 
    ve_catetouno=int(input("Digite cateto uno:"))
    ve_catetodos=int(input("Digite cateto dos:"))
     
     #procesos
     
    vps_radicando=math.pow(ve_catetouno,2) + math.pow(ve_catetodos,2)
    vps_hipotenusa=math.sqrt(vps_radicando)
    print("Hipotenusa:",vps_hipotenusa)
   #llamdo de la funcion  
f_titulo()
f_calcularhipotenusa()