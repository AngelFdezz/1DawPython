"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

10. Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
"""
chain = input("Dime una cadena: ")
character = input("Dime un character: ")
num_characters = 0

while len(character) != 1:
    character = input("Error. Dime solo un character: ")

is_character = False

for i in range(len(chain) + 1):
    character_to_check = chain.lower()[i:i + len(character)]
    if character_to_check == character.lower():
        is_character = True
        num_characters += 1
if is_character:
    print()
    print(f"Hay {num_characters} veces repetidas el carácter {character}")
else:
    print()
    print("No esta el carácter introducido")
