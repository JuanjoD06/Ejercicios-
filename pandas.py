# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:23:06 2021

@author: juanj
"""

import pandas as pd

df_archivoExcel = pd.read_excel('Poblacion_Area.xlsx')
print(df_archivoExcel)


Totalarea = df_archivoExcel['AREA'].sum()
print("Total area del pais : ",Totalarea)

maxs = df_archivoExcel['POBLACION'].max()
print("El departamento con mayor poblacion es: Bogota con",maxs,"Habitantes")

mins = df_archivoExcel['POBLACION'].min()
print("El departamento con menor poblacion es: Guainia con",mins,"Habitantes")

medias = df_archivoExcel['AREA'].mean()
print("Media de area",medias)

df_archivoExcel.plot.bar(x='DEPARTAMENTO',y='POBLACION')

df_archivoExcel.plot.bar(x='DEPARTAMENTO',y='AREA')

df_archivoExcel.plot.barh(x='DEPARTAMENTO',y='POBLACION')

df_archivoExcel.plot.barh(x='DEPARTAMENTO',y='AREA')

df_archivoExcel.plot.pie(x='DEPARTAMENTO',y='POBLACION')

df_archivoExcel.plot.pie(x='DEPARTAMENTO',y='AREA')










