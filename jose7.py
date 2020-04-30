# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:00:07 2020

@author: josel
"""


abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Aqui pongo toda la parte de codigo backend
def cifracesar(texto,key):
    
    texto_cifrado=""

    for letra in texto:
        
        nueva_posicion=(abecedario.index(letra)+key)
        
      
        if (nueva_posicion>26):
            nueva_posicion=nueva_posicion-26
            nueva_posicion=nueva_posicion-1

        letra_cifrada=abecedario[nueva_posicion]
        texto_cifrado+=letra_cifrada

    return texto_cifrado

   
#Voy a poner todos los print aqui
print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


cifrado=cifracesar(texto_claro,clave)
print ("El texto cifrado es:",cifrado)