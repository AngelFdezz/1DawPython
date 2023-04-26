"""
10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de
los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.

* 30% de la calificación del examen final.

* 15% de la calificación de un trabajo final.
Fecha: 9/10/2022.

Objetivo:
Crear las variables de parciales y hacer su promedio
-crear variable de examen final y trabajo final
-hacer los porcentajes de cada nota y sumarlos para saber su nota final
-Mostrarlo en pantalla.
"""
parcial1 = float(input("Introduce la nota del parcial 1: "))
parcial2 = float(input("Introduce la nota del parcial 2: "))
parcial3 = float(input("Introduce la nota del parcial 3: "))
total_parciales = (parcial3 + parcial2 + parcial1)/3
examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))

nota_final = total_parciales*0.55 + examen_final*0.3 + trabajo_final*0.15

print("Su nota final de", round(nota_final, 3))