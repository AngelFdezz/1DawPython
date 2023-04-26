"""
Autor: Angel Fernandez Ariza.
Fecha: 8/10/2022.

19. Escribir un programa para calcular la nota final de un estudiante, considerando que:

cada respuesta correcta suma 5 puntos
cada respuesta incorrecta suma -1 puntos
cada respuesta en blanco suma 0 puntos.
Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas puedan cambiar en el
futuro?

Objetivo:

-Mostrarlo en pantalla.
"""
num_respuestas = int(input("¿Cuantas preguntas quieres que tenga el examen?: "))
num_respuestas_correctas = int(input(f"¿Cuantas respuestas correctas quieres que tenga el examen de esas "
                                     f"{num_respuestas} preguntas?: "))
num_respuestas_incorrectas = int(input(f"¿Cuantas respuestas incorrectas quieres que tenga el examen de esas "
                                       f"{num_respuestas - num_respuestas_correctas} preguntas restantes?: "))
print(f"El examen trendrá {num_respuestas - num_respuestas_correctas - num_respuestas_incorrectas} preguntas en blanco")

puntuacion_total = (num_respuestas_correctas * 5 - num_respuestas_incorrectas)
nota_final = 10 * puntuacion_total / (num_respuestas*5)

print("Su nota es de:", nota_final)
