"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

7. Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres
cosas:

El exponente sea positivo, solo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
base = int(input("Dime un número: "))
exp = int(input("Dime su exponente: "))

if exp > 0:
    print(f"El resultado de {base} elevado a {exp} es de {base**exp}")
elif exp == 0:
    print(f"El resultado de {base} elevado a {exp} es de 1")
else:
    print(f"El resultado de {base} elevado a {exp} es de {1/(base ** abs(exp))}")

