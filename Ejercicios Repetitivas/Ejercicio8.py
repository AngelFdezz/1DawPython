"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

8. Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo ti.
"""
import time

segundos = 0
minutos = 0
horas = 0


while horas <= 24:
    time.sleep(1)
    segundos += 1
    print(8 * "\b", end="")  # ponemos el cursor al principio de la línea
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
