"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

Escribe un programa que lea un número e indique si es par o impar.
Objetivo:
-pedir numero y almacenarlo en una variable
if % 2 = 0  es par else impar
-Mostrarlo en pantalla.
"""

num = int(input("Dime un número: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
