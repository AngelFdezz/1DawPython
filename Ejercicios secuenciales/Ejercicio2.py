"""
2. Calcular el perímetro y área de un rectángulo dada su base y su altura.
Autor: Angel Fernandez Ariza.
Fecha: 8/10/2022.

Objetivo: Pedir la base y la altura del rectangulo, almacenarlas cada una en una variable, despues hacer los cálculos
del área y el perímetro y almacenar cada valor en su variable.
"""

base = float(input("Dime la base: "))
altura = float(input("Dime la altura: "))

perimetro = 2*base + 2*altura
area = base * altura

print("El perímetro es", perimetro, "y el área es", area)


