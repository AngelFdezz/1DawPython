"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina
cuando se introduce un espacio.
"""
vocales = "AEIOUÁÉÍÓÚ"
while True:
    character = input("Introduce un carácter: ")
    if character.upper() in vocales:
        print("VOCAL")
    else:
        print("NO VOCAL")
    if character == " ":
        break
