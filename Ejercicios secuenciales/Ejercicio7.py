"""
7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Autor: Angel Fernandez Ariza.
Fecha: 9/10/2022.

Objetivo:
-Pedir una cantidad de minutos y almacenarla en una variable.
-hacer la conversion de esos minutos a horas y almacenarlo en una variable como entero.
-Almacenar en otra variable el resto de la conversion de minutos a horas.
-Mostrarlo en pantalla.
"""

minutos = int(input("Dime una cantidad de minutos: "))

horas = minutos//60

minutos2 = minutos % 60

print(minutos, "minutos son", horas, "horas y", minutos2, "minutos")
