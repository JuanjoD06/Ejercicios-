# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:10:39 2021

@author: juanj
"""

cal1 = int(input("Ingrese calificacion del primer bimestre:"))
cal2 = int(input("Ingrese calificacion del primer bimestre:"))
cal3 = int(input("Ingrese calificacion del segundo bimestre:"))
cal4 = int(input("Ingrese calificacion del segundo bimestre:"))

promedio = (cal1 + cal2 + cal3 + cal4) / 4

if promedio >= 3.5:
    print("Aprobado")

else:
    print("reprobado")


  