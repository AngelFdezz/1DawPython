"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

4.Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso
 en caso contrario.
Objetivo:

-Mostrarlo en pantalla.
"""

num1 = float(input("Dime un número: "))
num2 = float(input("Dime otro número: "))

if num2 != 0:
    print(f"La division de {num1} entre {num2} es {round(num1/num2, 3)}")
else:
    print("El segundo número no puede ser 0")
    num2 = float(input("Dime otra vez el número: "))
    print(f"La division de {num1} entre {num2} es {round(num1 / num2, 3)}")
