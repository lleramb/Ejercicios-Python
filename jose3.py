# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:23:00 2020

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
  
  
# for i in range(edad1+1):
    
#     print("Que no cumpla",i)

# else:
  
#     print ("!!Que si cumple añoss!!!")


lista=[nombre1,tegusta1,edad1]

for variables in lista:
      print('Su nombre es: ', variables,)
