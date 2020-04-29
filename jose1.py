# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:12:05 2020

@author: josel
"""

print ("BIENVENIDO A EMPAREJANDO.COM")

nombre1= input("Tu nombre:")
ano1= int(input( "¿Año de nacimiento?" ))
tegusta1= input("¿Te gusta taburete?")

edad1  =  2020 - ano1

print ("hola", nombre1, ". Si no me equivoco tienes", edad1, "años.")

if tegusta1 == "si" or tegusta1 == "Si":
  print('OK Boomer, lo tuyo va a ser un caso difícil.')
elif tegusta1 == "no" or tegusta1 == "No":
  print('Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.')
