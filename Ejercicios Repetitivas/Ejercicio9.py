"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

9. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos
mostrar.
"""
import math

# Pedimos datos
while True:  # repetir
    num_primes_to_show = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if num_primes_to_show > 0:
        break  # condición de salida del ciclo

# Proceso

# el primer primo es 2, los otros son todos impares...
print("1º: 2")
num_primes_displayed = 1

# ...a partir de 3
prime_candidate = 3
while num_primes_displayed < num_primes_to_show:
    # pienso que es primo hasta que encuentre con que dividirlo
    is_primo = True
    # ya sabemos que es impar
    divider = 3  # no empiezo en 2 porque sé que "candidato_a_primo" es impar
    while divider <= math.sqrt(prime_candidate):
        # si la división da exacta...
        if prime_candidate % divider == 0:
            # ...ya no es primo, acabamos
            is_primo = False
            break
        divider += 2  # va al siguiente impar, no necesito comprobar el par
    # si "candidato_a_primo" es primo, lo imprimo y contabilizo uno más
    if is_primo:
        num_primes_displayed += 1
        print(f"{num_primes_displayed}º: {prime_candidate}")
    prime_candidate += 2  # el siguiente sigue siendo impar
    