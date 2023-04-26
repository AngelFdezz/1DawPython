"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

4. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""
num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))

if num1 > num2:
    num1, num2 = num2, num1
if num1 % 2 == 0:
    num = num1
else:
    num = num1 + 1
print()
print(f"Los números pares que hay entre {num1} y {num2} son: ")
print()
while num2 >= num:
    print(num)
    num += 2
