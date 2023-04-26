"""Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las
palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente."""
numbers = []
amount_of_numbers = 10

for i in range(amount_of_numbers):
    ext = int(input(f"Dime el {i + 1}º número: "))
    numbers.append(ext)
max_number = max(numbers)
min_number = min(numbers)

for i in range(amount_of_numbers):
    if numbers[i] == max_number:
        numbers[i] = str(numbers[i]) + " máximo"
    if numbers[i] == min_number:
        numbers[i] = str(numbers[i]) + " mínimo"
    print(numbers[i])
