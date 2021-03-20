# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:26:14 2021

@author: juanj
"""
#Area de declaracion de variables
var_e_nom = "***"
var_e_bas = 0.0
var_e_for = 0.0
var_e_pas = 0.0
# Leer nombre
var_p_s_medest = 0.0

#Digite
var_e_nom = input("Digite el nombre del estudiante:")

#Ciclo while
while (var_e_nom != "***"):
      #Inicio del ciclo
      var_e_bas = float(input("Definitiva Basic: "))
      var_e_for = float(input("Definitiva Fortran: "))
      var_e_pas = float(input("Definitiva Pascal: "))
      
      #Proceso que calcula la media del estudiante
      var_p_s_medest = (var_e_pas + var_e_bas + var_e_for)/3
      print("Su media es:",var_p_s_medest)
      var_e_nom = input("Digite nombre del estudiante:")