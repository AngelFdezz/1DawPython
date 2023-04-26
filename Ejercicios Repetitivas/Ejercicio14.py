"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

14. Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
"""

STRING = "¿Es Victor un buen delegado?"
substring_to_search = input(f"Dime una subcadena para comprobar si esta en '{STRING}': ")

last_index_to_check = len(STRING) - len(substring_to_search) + 1
is_substring = False

for i in range(last_index_to_check):
    substring_to_check = STRING[i:i + len(substring_to_search)]
    if substring_to_search == substring_to_check:
        is_substring = True
        break

if is_substring:
    print(f"Se ha encontrado la subcadena '{substring_to_search}' en '{STRING}'")
else:
    print("No se ha encontrado")
