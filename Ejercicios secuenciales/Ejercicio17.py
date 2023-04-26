"""
17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra
ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
Fecha: 10/10/2022.

Objetivo:

-Mostrarlo en pantalla.
"""
hora_s = int(input("Dame una hora de salida: "))
minutos_s = int(input("Dame una minutos de salida: "))
segundos_s = int(input("Dame unos segundos de salida: "))
tiempo_segundos = int(input("Dame los segundos que quieres que tarde en llegar: "))

hora_s_a_segundos = hora_s * 3600 + minutos_s * 60 + segundos_s
tiempo_llegar = hora_s_a_segundos + tiempo_segundos

hora_llegada = tiempo_llegar // 3600
minutos_llegada = (tiempo_llegar % 3600) // 60
segundos_llegada = (tiempo_llegar % 3600) % 60

print(f"Llegara a las {hora_llegada} horas, {minutos_llegada} minutos y {segundos_llegada} segundos")
