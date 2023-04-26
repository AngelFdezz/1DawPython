"""
Autor: Angel Fernandez Ariza.
Fecha: 10/11/2022.

4. Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la
mala suerte son el resto: el 0, el 1, el 2, el 4, el 5 y el 6. Un número es afortunado si contiene más
números de la suerte que de la mala suerte. Realiza un programa que diga si un número introducido
por el usuario es afortunado o no.
Ejemplo 1: Introduzca un número: 772
El 772 es un número afortunado.
Ejemplo 2: Introduzca un número: 7720
El 7720 no es un número afortunado.
Ejemplo 3: Introduzca un número: 43081
El 43081 no es un número afortunado.
Ejemplo 4: Introduzca un número: 888
El 888 es un número afortunado.
Ejemplo 5: Introduzca un número: 1234
El 1234 no es un número afortunado.
Ejemplo 6: Introduzca un número: 6789
El 6789 es un número afortunado.
"""
contador_num_suerte = 0
contador_num_no_suerte = 0
num = input("Por favor, introduzca un número de la suerte positivo: ")
num_suerte = "3789"
while not num.isdigit() or int(num) < 0:
    num = input("No has introducido un carácter válido,vuelve a introducir un número de la suerte: ")

for i in num:
    if i in num_suerte:
        contador_num_suerte += 1
    else:
        contador_num_no_suerte += 1

if contador_num_suerte > contador_num_no_suerte:
    print(f"El {num} es un número afortunado")
else:
    print(f"El {num} no es un número afortunado")
