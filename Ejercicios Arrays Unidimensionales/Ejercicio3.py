"""
Define tres arrays de 20 números enteros cada uno, con nombres número, cuadrado y cubo. Carga el array número con
valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el
array número. En el array cubo se deben almacenar los cubos de los valores que hay en número. A continuación, muestra
el contenido de los tres arrays dispuesto en tres columnas.
"""
from random import randrange

numero = []
cuadrado = []
cubo = []

for i in range(20):
    num_random_for_numero = randrange(0, 100)
    numero.append(num_random_for_numero)

for j in numero:
    auxiliar = j ** 2
    cuadrado.append(auxiliar)

for k in numero:
    auxiliar = k ** 3
    cubo.append(auxiliar)

print(f" El array numero:   {numero}")
print(f" El array cuadrado: {cuadrado}")
print(f" El array cubo:     {cubo}")
