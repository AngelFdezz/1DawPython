"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

10. Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en
uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes_interiores
interiores
concéntricas
"""
import math

x1 = float(input("Dime el punto central x1 de una circunferencia: "))
y1 = float(input("Dime el punto central y1 de una circunferencia: "))

x2 = float(input("Dime el punto central x2 de otra circunferencia: "))
y2 = float(input("Dime el punto central y2 de otra circunferencia: "))

r1 = float(input("Dime el radio r1 de la primera circunferencia: "))
r2 = float(input("Dime el radio r2 de la segunda circunferencia: "))

distance_central_point = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# EXTERIORES
if distance_central_point > (r1 + r2):
    print("Circunferencias exteriores")

# Circunferencias secantes
elif (r1 + r2) > distance_central_point > abs(r1 - r2):
    print("Circunferencias secantes")

# Circunferencias interiores
elif 0 < distance_central_point < abs(r1 - r2):
    print("Circunferencias interiores")

# Circunferencias tangentes exteriores
elif distance_central_point == (r1 + r2):
    print("Circunferencias tangentes exteriores")

# Circunferencias tangentes interiores
elif distance_central_point == abs(r1 - r2):
    print("Circunferencias tangentes interiores")

# Circunferencias concéntricas
elif distance_central_point == 0:
    print("Circunferencias concéntricas")
else:
    print("Esta situación no se puede dar")
