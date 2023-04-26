"""
9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
finalmente por su compra.
Fecha: 9/10/2022.

Objetivo:
-Crear variables compra, descuento y total_compra
-Aplicarle un 15% a la variable compra y restárselo a la compra
-Mostrarlo en pantalla.
"""
compra = float(input("Introduce un precio de compra: "))
descuento = compra*0.15
total_compra = compra - descuento

print("El total que deberá pagar con el descuento es de", total_compra, "€")
