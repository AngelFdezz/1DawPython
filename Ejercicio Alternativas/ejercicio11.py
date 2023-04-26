"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

11. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguientes:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si solo dos lados del triángulo son iguales entonces es isósceles.
Sí los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""
A = float(input("Dime el lado A de un triángulo: "))
B = float(input("Dime el lado B de un triángulo: "))
C = float(input("Dime el lado C de un triángulo: "))

if A**2 == B**2 + C**2:
    print("El triángulo es rectángulo")
elif B**2 == A**2 + C**2:
    print("El triángulo es rectángulo")
elif C**2 == B**2 + A**2:
    print("El triángulo es rectángulo")
elif A == B != C or A == C != B or C == B != A:
    print("El triángulo isósceles")
elif A == B == C:
    print("El triángulo es equilátero")
else:
    print("El triángulo es escaleno")
