"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o
 igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo
 sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
"""

note = int(input("Dime una nota de 1-10: "))
age = int(input("Dime tu edad: "))
sex = input("Dime tu sexo(M/F): ")

if note >= 5 and age >= 18 and sex.upper() == "F":
    print("ACEPTADA")
elif note >= 5 and age >= 18 and sex.upper() == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADO")
