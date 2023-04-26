"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

6. Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
resultado de la potencia. No se puede utilizar el operador de potencia ni la función.
"""

print("Cálculo de la potencia")
print("----------------------")

# Inicializamos variables
power = 1

# Pedimos datos
base = float(input("Base: "))
exponent = int(input("Exponente: "))

# Cálculos
for _ in range(abs(exponent)): # en Python podemos por _ si no hace falta variable de control
    power *= base

# Si el exponente es negativo calculamos la inversa
if exponent < 0:
    power = 1 / power

# Salida
print(f"\n{base} elevado a {exponent} es {power}")
