"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos
A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño, se requiere
determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B,
se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realce un algoritmo para
determinar la ganancia obtenida.
"""

price = 2
kilos = float(input("Dime cuantos quilos quieres: "))
type_uva = input("Que tipo vas a vender(A/B): ")
size = int(input("¿Que tamaño de uva quieres?(1/2): "))
uva_a_1 = 0.2
uva_a_2 = 0.3
uva_b_1 = 0.3
uva_b_2 = 0.5

if type_uva.upper() == "A" and size == 1:
    print(f"La ganancia es de {kilos * price + kilos * uva_a_1}€")
elif type_uva.upper() == "A" and size == 2:
    print(f"La ganancia es de {kilos * price + kilos * uva_a_2}€")
elif type_uva.upper() == "B" and size == 1:
    print(f"La ganancia es de {kilos * price - kilos * uva_b_1}€")
else:
    print(f"La ganancia es de {kilos * price - kilos * uva_b_2}€")
