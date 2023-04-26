"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

6. Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
-Mostrarlo en pantalla.
"""
cadena = input("Dime una letra: ")

if len(cadena) > 1 and cadena.isalpha():
    print("Has introducido mas de un valor")
    if cadena.upper() == cadena:
        print(f"{cadena} es mayúscula")
    elif cadena.lower() == cadena:
        print(f"{cadena} es minúscula")
else:
    print("Has introducido un valor incorrecto")
