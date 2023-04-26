"""
12. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la
distancia entre ellos.
Fecha: 9/10/2022.

Objetivo:
-Pedir los dos pares de numeros y almacenarlos en variables
-crear la variable distancia y almacenar en ella la distacia de los dos puntos del plano
-Mostrarlo en pantalla.
"""
import math

x1 = float(input("Dime el numero del eje x: "))
y1 = float(input("Dime su eje y: "))
print(f"Este sera el punto A: {x1},{y1}")

x2 = float(input("Dime otro numero del eje x: "))
y2 = float(input("Dime su eje y: "))
print(f"Este sera el punto B: {(x2)},{y2}")

distacia =  math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("La distancia de estos dos puntos es de", distacia)

