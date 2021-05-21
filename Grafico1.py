# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:09:38 2021

@author: juanj
"""

#Ejercicio que almacena en listas - procesa en funciones
# Declarar las librerias a usar para la solucion
import matplotlib.pyplot as plt

#Generar las listas con los datos incializados
nombreProducto=['Ron','Aguardiente','vino','cerveza']
existenciaProducto=[75,50,100,150]

#Funciones que resuelven el problema

def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    print("Total Existencias: ",sumaExistencias)

        
def f_calc_tot_existencias_2():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)


#  FunciÃ³n que calcula el promedio de las existencias
def f_calc_prom_existencias():
    promExistencias = f_calc_tot_existencias_2()/len(existenciaProducto)
    return(promExistencias)
        

#Llamado a las funciones que realizan los calculos
f_calc_tot_existencias

print("Total Existencias 2: ",f_calc_tot_existencias_2())

print("Promedio de Existencias : ",f_calc_prom_existencias())


#Graficar Informacion
fig, ax =plt.subplots()

#Definir el titulo grafico 

ax.set_title('Grafico de existencias de producto')
ax.set_xlabel("Productos")
ax.set_ylabel("Existencias")

#Crear el grafico
plt.bar(nombreProducto,existenciaProducto)

#Publico el grafico 
plt.show()