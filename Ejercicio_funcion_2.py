# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:08:42 2021

@author: juanj
"""
def f_titulo():
    print("Calculo valor factura")
#factura de venta

def f_valorFactura():
#Definicion de variables
    ve_nomArt = ""
    ve_canArt = 0
    ve_valUniArt = 0.0
    vps_NetPag = 0.0
    vps_ivaPag = 0.0
    vps_totPag = 0.0
    cons_porIva = 0.19


#Entrada de Datos
    ve_nomArt = input("Articulo:")
    ve_canArt = int(input("Cantidad:"))
    ve_valUniArt = float(input("Valor unitario:"))

#procesos
    vps_NetPag=ve_canArt * ve_valUniArt
    vps_ivaPag=vps_NetPag * cons_porIva
    vps_totPag=vps_NetPag + vps_ivaPag
    
#salidas
    print("Neto:",vps_NetPag)
    print("Iva:", vps_ivaPag)
    print("Total:",vps_totPag)

#Llamado a la funcion
f_titulo()
f_valorFactura()
