"""
5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Autor: Angel Fernandez Ariza.
Fecha: 8/10/2022.

Objetivo:
-Pedir la cantidad de grados F y almacenarlo en una variable
-Pasar los grados F a C y almacenarlo en otra variable
-Mostralo en pantalla"""

gradosF = int(input("Dime una cantidad de grados Fahrenheit: "))

gradosC = round((gradosF - 32) * 5/9, 4)

print(gradosF, "grados Fahrenheit son", gradosC, "grados Celsius")
