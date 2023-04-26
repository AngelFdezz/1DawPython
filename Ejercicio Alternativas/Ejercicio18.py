"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.
"""
num1 = int(input("Introduce un dia de la semana del 1-7: "))

if num1 >= 1 and num1 <= 7:
    if num1 == 1:
        print("Lunes")
    elif num1 == 2:
        print("Martes")
    elif num1 == 3:
        print("Miércoles")
    elif num1 == 4:
        print("Jueves")
    elif num1 == 5:
        print("Viernes")
    elif num1 == 6:
        print("Sábado")
    else:
        print("Domingo")
else:
    print("No has introducido un valor correcto")
