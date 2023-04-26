"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

16. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que este
dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80 céntimos por minuto
 los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de tarde,
10%. Realce un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realza una llamada.
"""


import sys

duration = int(input("¿Cuánto time dura la llamada?: "))
is_sunday = input("¿Es Domingo? (S/N): ")
if is_sunday.upper() == "N":
    turn = input("¿Qué turno: Mañana o Tarde? (M/T)?: ")
elif is_sunday.upper() != "S":
    print("La respuesta era S ó N, ha dado una distinta. Abortamos...", file=sys.stderr)
    exit(1)

# Proceso
if duration <= 5:
    cost = duration * 100
elif duration <= 8:
    cost = (duration - 5) * 80 + 500
elif duration <= 10:
    cost = (duration - 8) * 70 + 240 + 500
else:
    cost = (duration - 10) * 50 + 140 + 240 + 500

# impuestos
if is_sunday.upper() == "S":
    cost += cost * 0.03
elif turn.upper() == "M":
    cost += cost * 0.15
else:
    cost += cost * 0.10

# Salida
print("El coste de la llamada:", cost / 100, "euros.")
