"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe
 informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""
positive = 0
negative = 0
zero = 0

total_num = int(input("¿Cuántos números vas a introducir?: "))

for i in range(total_num):
    number = int(input(f"Número {i + 1}: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1
print()
print(f"Has introducido {positive} números positivos")
print(f"Has introducido {negative} números negativos")
print(f"Has introducido {zero} ceros")
