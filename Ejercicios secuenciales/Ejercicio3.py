"""
3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
Autor: Angel Fernandez Ariza.
Fecha: 8/10/2022.

Objetivo:
-Pedir el valor de los catetos y almacenarlos en variables
-aplicar la formula para calcular la hipotenusa y almacenarlo en una variable
-mostrar el valor de la hipotenusa aplicandole la raiz cuadrada
"""
import math

cateto1 = float(input("Dime el valor del cateto 1: "))
cateto2 = float(input("Dime el valor del cateto 2: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa es", hipotenusa)
