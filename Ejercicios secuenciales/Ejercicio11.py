"""
11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que
el resultado sea siempre positivo).
Fecha: 9/10/2022.

Objetivo:
-Pedir dos numeros y almacenarlos en variables
-almacenar la distancia en otra variable aplicandole el valor absoluto
-Mostrarlo en pantalla.
"""
numero1 = float(input("Dime un número: "))
numero2 = float(input("Dime otro número: "))

distancia = abs(numero1 - numero2)

print("La distancia que hay entre estos dos números es de", distancia)
