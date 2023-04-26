"""
20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

Objetivo:
-pedir al usuario cuantas monedas quiere de cada tipo de moneda y almacenarlo en variables
-calcular cuantos euros tiene segun cuantas monedas de euro tenga y almacenarlo en variable
-hacer lo miso con clos centimos
-calcular los euros totales que tenga si los centimos valen euros es decir hacer div entera a cent y sumar a euros
-hacer resto de la conversion de centimos a euros para saber cuantos centimos tenemos
-Mostrarlo en pantalla.
"""

e2 = int(input("¿Cuantas monedas de 2€ tienes?:"))
e1 = int(input("¿Cuantas monedas de 1€ tienes?:"))
c50 = int(input("¿Cuantas monedas de 50 centimos tienes?:"))
c20 = int(input("¿Cuantas monedas de 20 centimos tienes?:"))
c10 = int(input("¿Cuantas monedas de 10 centimos tienes?:"))

dinero_euros = e2 * 2 + e1
dinero_centimos = c50 * 50 + c20 * 20 + c10 * 10
dinero_euros_total = dinero_centimos // 100 + dinero_euros
dinero_centimos_total = dinero_centimos % 100

print(f"Tienes {dinero_euros_total} euros y {dinero_centimos_total} centimos")
