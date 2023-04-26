"""
13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna
función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
Fecha: 9/10/2022.

Objetivo:
-almacenar el numer
-hacer su riaz cuadrada
-hacer una variable para la raiza cubica y hacer como el numero elevado a 1/3
-Mostrarlo en pantalla.
"""
import math

num = float(input("Dime un número: "))

print("Su raíz cuadrada es", math.sqrt(num))
raiz_cubica = num**(1/3)
print("Su raíz cubica es", raiz_cubica)
