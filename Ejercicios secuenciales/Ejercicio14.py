"""
14. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
Fecha: 9/10/2022.

Objetivo:
-pedir un número de dos digitos y almacenarlo n una variable
-crear dos variables para almacenar la primera posicion y otro para la segunda de la variable num
-crear otra variable para hacer el numero invertido
-Mostrarlo en pantalla.
"""
num = input("Dime un numero de dos cifras: ")
digito1 = num[0]
digito2 = num[1]
num_invertido = digito2 + digito1
print("El numero invertido es", num_invertido)

