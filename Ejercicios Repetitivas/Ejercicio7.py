"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

7. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €,
el tercero 40 € y así sucesivamente.
Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.

"""
MONTHS = 20
FIRST_PAYMENT = 10

total_payment = 0
payment_month = FIRST_PAYMENT

for mes in range(MONTHS):
    print(f"Pago mes {mes+1:2d}: {payment_month:8,d}€")
    total_payment += payment_month
    payment_month *= 2

print(f"\nTotal a pagar: {total_payment:,d}€")
