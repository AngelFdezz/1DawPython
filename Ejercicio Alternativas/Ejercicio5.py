"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

5. Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta
que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Objetivo:

-Mostrarlo en pantalla.
"""

person1 = int(input("Dime la edad de una Rafa: "))
person2 = int(input("Dime la edad de otra Paco: "))

if person1 > person2:
    print("Rafa es mayor que Paco")
elif person2 > person1:
    print("Paco es mayor que Rafa")
else:
    print("Rafa y Paco tienen la misma edad")
