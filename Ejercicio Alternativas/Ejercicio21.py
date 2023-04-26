"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

21. Realiza un programa que pida tres números enteros y diga cuál es el mayor.
"""


num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))
num3 = int(input("Dime el número 3: "))

if num1 > num2 and num1 > num3:
    print(f"El mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El mayor es {num2}")
elif num3 > num2 and num3 > num1:
    print(f"El mayor es {num3}")
elif num1 == num2 == num3:
    print("Los tres son iguales")
else:
    print("Escribe números que no sean iguales")



