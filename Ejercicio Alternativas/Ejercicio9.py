"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si el
carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o
acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter»
si el usuario ha introducido más de un carácter.
"""

character = input("Dime un carácter: ")

if len(character) == 1:
    if character in "´.:;,.-_¨(){}?¿¡!/~·":
        print(f"{character} es un signo de puntuación")
    elif character.isalpha():
        print(f"{character} es una letra")
    elif character.isdigit():
        print(f"{character} es un dígito")
    else:
        print("Es otro carácter")
else:
    print("No es un carácter")
