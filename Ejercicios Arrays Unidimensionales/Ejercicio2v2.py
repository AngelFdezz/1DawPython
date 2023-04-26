"""
Programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que se introduce
es el último en mostrarse y viceversa.
"""

AMOUNT_NUMBERS_TO_READ = 10
numbers = []

for i in range(AMOUNT_NUMBERS_TO_READ):
    n = int(input(f"Dame el número que estará en la posición {i + 1}: "))
    numbers.append(n)

for n in numbers[::-1]:
    print(n)
