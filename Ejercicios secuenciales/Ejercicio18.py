"""
18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
Fecha: 10/10/2022.

Objetivo:

-Mostrarlo en pantalla.
"""
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

Ini_nombre = nombre[0]
Ini_apellido1 = apellido1[0]
Ini_apellido2 = apellido2[0]

print(f"Las iniciales de su nombre completo son: {Ini_nombre}{Ini_apellido1}{Ini_apellido2}")
