"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

23. Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al
 primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más
 cercano al 2 es el 1.
"""
print("Este programa pide 5 números enteros y dice cual de ellos es más cercano al primero introducido")
print("-----------------------------------------------------------------------------------------------")

num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))
num3 = int(input("Dame otro número entero: "))
num4 = int(input("Dame otro número entero: "))
num5 = int(input("Dame otro número entero: "))

if (num1-num2)*(num1-num2) <= (num1-num3)*(num1-num3):
    mas_cercano = num2
else:
    mas_cercano = num3

if (num1-num4)*(num1-num4) <= (num1-num5)*(num1-num5):
    mas_cercano2 = num4
else:
    mas_cercano2 = num5

if mas_cercano <= mas_cercano2:
    print(f"El más cercano a {num1} es {mas_cercano}")
else:
    print(f"El más cercano a {num1} es {mas_cercano2}")
