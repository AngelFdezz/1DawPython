"""
        Ejercicio 2:
            Escribe un programa que sea capaz de leer el fichero anterior y lo muestre por la pantalla.
    Autor: Angel Fernandez
    Curso: 2022-2023
"""

archivo = open('primos.txt', 'r')
lista = archivo.readlines()
for i in lista:
    print(i)
archivo.close()
