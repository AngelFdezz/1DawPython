"""
Autor: Angel Fernandez Ariza.
Fecha: 10/11/2022.

1. Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El
programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo
siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto
satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.
Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera
anormal con un mensaje de error.
"""
import sys

PIN = 1234
num_attempt = 0

while num_attempt < 4:
    attempt = input("Dime una combinación de 4 dígitos para intentar abir la caja fuerte: ")
    num_attempt += 1
    if not len(attempt) == 4:
        print("Lo siento no has introducido un pin válido", file=sys.stderr)
        exit(1)
    elif not attempt.isdigit():
        print("Lo siento no has introducido un pin válido", file=sys.stderr)
        exit(1)
    elif int(attempt) == PIN:
        print("Has acertado, la caja fuerte se ha abierto satisfactoriamente")
        break
    elif num_attempt == 4:
        print("Se te acabaron los intentos, no has abierto la caja")
        break
    else:
        print("Lo siento, esa no es la combinación")
        print()

