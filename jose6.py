# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 21:57:33 2020

@author:  josel
"""
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Welcome to my Cifrado!!")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


texto_cifrado=""

for letra in texto_claro:
    nueva_posicion=(abecedario.index(letra)+clave) % 27
    letra_cifrada=abecedario[nueva_posicion]
    texto_cifrado+=letra_cifrada

print(texto_cifrado)
    