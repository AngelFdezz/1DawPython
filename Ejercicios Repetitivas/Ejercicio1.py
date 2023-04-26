"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

1. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A
continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, a demás
de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
(además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había
generado.
"""
import random

STARTING_NUMBER = 1
FINAL_NUMBER = 100
MAXIMUM_TRIES = 10

# Inicializamos
numero_a_adivinar = random.randint(STARTING_NUMBER, FINAL_NUMBER)
intentos_que_quedan = MAXIMUM_TRIES

# Proceso
while True:  # implementación ciclo post condición REPETIR
    numero_introducido = int(input(f"Te quedan {intentos_que_quedan} intentos. Introduce un número entre 1 y 100: "))

    # pista (si no acierta) para que le sea más fácil adivinar
    if numero_introducido < numero_a_adivinar:
        print(f"{numero_introducido} es menor que el número a adivinar.")
    elif numero_introducido > numero_a_adivinar:
        print(f"{numero_introducido} es mayor que el número a adivinar.")

    intentos_que_quedan -= 1    # hemos consumido un intento

    # salida ciclo
    if numero_introducido == numero_a_adivinar or intentos_que_quedan == 0:  # acabo si adivino o supero los intentos
        break

# Mostramos si acertó o no
if numero_introducido == numero_a_adivinar:  # ha adivinado
    print(f"Has adivinado el número en {MAXIMUM_TRIES - intentos_que_quedan} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {numero_a_adivinar}")
