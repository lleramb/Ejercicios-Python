# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:00:07 2020

@author: josel
"""

def cifracesar(texto,clave):
      
texto = input("Mensaje > ").upper()


clave = int(input("Desplazamiento > "))


abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


cifrado = ""



for l in texto:

    if l in abc:
        pos_letra = abc.index(l)
      
        nueva_pos = (pos_letra + clave) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        
        cifrado+= l

print("Mensaje cifrado:", cifrado)

texto = input("Mensaje cifrado > ").upper()


abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


for i in range(28):
    descifrado = ""
    for l in texto:
        if l in abc:
            pos_letra = abc.index(l)
            nueva_pos = (pos_letra - i) % len(abc)
            descifrado += abc[nueva_pos]
        else:
            descifrado+= l
    msj = (f"ROT-{i}:", descifrado)
    print(msj)
    

      print (cifracesar)