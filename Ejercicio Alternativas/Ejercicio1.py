"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

1.Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Objetivo:
-Pedir dos numeros
-Almacenarlosen variables
-hacer if

-Mostrarlo en pantalla.
"""

num1 = float(input("Dime un número: "))
num2 = float(input("Dime otro número: "))

if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}")
else:
    print("Los numeros son iguales")
