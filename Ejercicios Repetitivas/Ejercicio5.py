"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

5. Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
 superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
 informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.
"""

# Inicializamos
numbers_out_range = 0    # cuenta los números introducidos fuera del intervalo
there_are_numbers_at_the_limits = False    # interruptor que nos dice si hemos introducido algún extremo
sum_in_range = 0    # suma de los números introducidos dentro del intervalo

# Pido el intervalo y me aseguro que el lim_inf introducido es menor que el lim_sup
# se podía haber hecho con un ciclo ITERAR (ver siguiente ejemplo)
lower_range = int(input("Introduce el límite inferior del intervalo: "))
upper_range = int(input("Introduce el límite superior del intervalo: "))
while lower_range > upper_range:
    print("El límite inferior no puede ser mayor al superior.")
    print("VUELVE a introducir los límites.\n")
    lower_range = int(input("Introduce (correctamente) el límite inferior del intervalo: "))
    upper_range = int(input("Introduce (correctamente) el límite superior del intervalo: "))

# Proceso
num = int(input("\nIntroduce un número (0, para salir): "))
while num != 0:
    if lower_range < num < upper_range:  # Pertenece al intervalo (num>lim_inf and num<lim_sup en otro lenguaje)
        sum_in_range += num
    else:  # No pertenece al intervalo
        numbers_out_range += 1
        # Número igual a alguno de los límites
        if num == lower_range or num == upper_range:
            there_are_numbers_at_the_limits = True
    num = int(input("Introduce un número (0, para salir): "))

# Resultados
print("\nRESULTADOS:")
print(f"La suma de los números dentro del intervalo es {sum_in_range}")
print(f"La cantidad de números fuera del intervalo es {numbers_out_range}")
if there_are_numbers_at_the_limits:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
