"""
Programa para comprobar que la función palotes() funciona bien.

"""
from Ejercicio5palotes import palotes

print("Conversor de números al sistema de palotes")
print("------------------------------------------")

n = int(input("Dame un número entero positivo: "))
print(f"{n} convertido al sistema de palotes es: {palotes(n)}")
