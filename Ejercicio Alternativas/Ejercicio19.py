"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

19.
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes
correspondiente.
"""

num = int(input("Dime un numero de mes del 1-12: "))

if 1 <= num <= 12:

    if num == 2:
        print("El mes tiene 28 dias")
    elif num % 2 == 0:
        print("El mes tiene 30 dias")
    elif num % 2 != 0:
        print("El mes tiene 31 dias")
else:
    print("Solo valen números del 1-12")
