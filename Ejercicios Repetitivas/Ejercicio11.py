"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

11. Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
 realiza un programa que cuente cuantas palabras tiene.
"""
phrase = input("Dime una frase: ")

pre_char = " "
word_count = 0
for current_char in phrase:
    if current_char != " " and pre_char == " ":
        word_count += 1
    pre_char = current_char
print(f"Hay {word_count} palabras separadas por espacios en '{phrase}'")
