# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:41:07 2021

@author: juanj
"""

def f_cargar():
    lista=[]
    for i in range (3):
        numero=int(input("Ingrese un numero:"))
        lista.append(numero)
    return lista

def f_generar_lista(lista):
    list_negativa=[]
    list_positiva=[]
    for i in range(len(lista)):
        if lista[i]<0:
            list_negativa.append(lista[i])
        else:
            if lista[i]>0:
                list_positiva.append(lista[i])
    return [list_negativa,list_positiva]
def f_imprimir(lista):
    for i in range(len(lista)):
        print(lista[i])

lista=f_cargar()
list_negativa,list_positiva=f_generar_lista(lista)
print("Lista con numeros negativos")
f_imprimir(list_negativa)
print("Lista con numeros positivos")
f_imprimir(list_positiva)
    