# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:17:58 2021

@author: juanj
"""
import math 

a = float(int(input("Ingrese coeficiente a:")))
b = float(int(input("Ingrese coeficiente b:")))
c = float(int(input("Ingrese coeficiente c:")))
discriminante = b**2-4*a*c

if discriminante >= 0:
    if discriminante == 0:
        x = -b/(2*a)
        print("La raiz unica es {:.3f}".format(x))
else:
    x1 = (-b+math.sqrt(discriminante))/(2*a)
    x2 = (-b+math.sqrt(discriminante))/(2*a)
    print ("la raiz x1 es {:.3f}".format(x1))
    print ("la raiz x2 es {:.3f}".format(x2))

else:
    discriminante = abs(discriminante)
    par_re = -b/(2*a)
    par_im = math.sqrt(discriminante)/(2*a)
    print("La raiz comp x1 es {:.3f}+{:.3f}i".format(par_re, par_im))
    print("La raiz comp x2 es {:.3f}+{:.3f}i".format(par_re, par_im))
    