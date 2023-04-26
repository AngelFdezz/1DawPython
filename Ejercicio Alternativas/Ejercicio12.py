"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

12. Escribir un programa que lea un año indicar si es bisiesto.
"""

year = int(input("Dime un año: "))

if year > 0 and year % 4 == 0:
    print("El año que has introducido es bisiesto")
elif year > 0 and year % 4 != 0:
    print("El año que has introducido no es bisiesto")
else:
    print("No has introducido un año valido")
