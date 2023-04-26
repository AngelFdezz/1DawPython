"""
15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los
valores de ambas variables y muestre cuanto valen al final las dos variables.
Fecha: 10/10/2022.

Objetivo:
-almacenar los dos valores en dos variables
-crear una variable para hcaer el intercambio
-Mostrarlo en pantalla.
"""

A = int(input("Dale un valor a A: "))
B = int(input("Dale un valor a B: "))
print("Ahora vamos a cambiar el valor de B a A y de A a B")

intercambio = A
A = B
B = intercambio

print("El nuevo valor de A es:", A)
print("El nuevo valor de B es:", intercambio)


