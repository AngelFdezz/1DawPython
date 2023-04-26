"""
        Ejercicio 1:
            Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero de texto.
            El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.
            El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
            palabras_sort.txt.
            Suponemos que cada palabra ocupa una línea.

    Autor: Angel Fernandez Ariza
    Curso: 2022-2023
"""
import sys

palabra1 = sys.argv[1]
palabra2 = sys.argv[2]
palabra3 = sys.argv[3]
palabra4 = sys.argv[4]

with open("holaleeme.txt", 'w') as archivo:
    archivo.write(palabra1 + "\n")
    archivo.write(palabra2 + "\n")
    archivo.write(palabra3 + "\n")
    archivo.write(palabra4 + "\n")

lista = []
with open("holaleeme.txt", 'r') as archivo2:
    recorre = archivo2.readlines()
    for i in recorre:
        lista.append(i)
lista.sort()
with open("holaleeme.txt", 'w') as archivo3:
    for j in lista:
        archivo3.write(j)
