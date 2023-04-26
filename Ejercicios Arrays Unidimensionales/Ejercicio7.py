"""
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los
elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1,
el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la
posición 0. Finalmente, muestra el contenido del array.

"""

TOTAL_NUMBERS = 5
numbers = [1, 2, 3, 4, 5]

# Pedimos los datos


# Rotamos una posición a la derecha
aux = numbers[-1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = aux
print("\nLista rotada una posición a la derecha:", numbers)
