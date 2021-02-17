# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:46:44 2021

@author: juanj
"""

usuario = int(input("ingrese valor de compra"))
iva = usuario * 0.19
descuento = usuario * 0.05

usuario_iva= usuario + iva

todo = usuario_iva - descuento


print ("el valor a pagar es : ", todo)