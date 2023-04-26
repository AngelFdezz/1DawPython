"""
Autor: Angel Fernandez Ariza.
Fecha: 8/10/2022.

16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás
viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus
respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido
al otro.

Objetivo:
-Pedir y almacenar velocidades y distancia
-Aplicar la fórmula de e = v/t despejando el tiempo y pasandolo a minutos.
-Mostrarlo en pantalla.
"""
print("Este programa pide dos velocidades distintas de dos vehiculos una mayor que otra, además pide la distancia "
      "entre estos para calcular cuanto tardar en pillar el coche de mas velocidad al otro")


v1 = float(input("Introduce una velocidad del primer coche: "))
v2 = float(input(f"Introduce una velocidad del segundo coche mayor a {v1}km/h: "))
distance = float(input("Introduce una distancia entre los coches(km): "))

time = round(60 * (distance / (v2 - v1)), 2)

print(f"El segundo coche tarda en pillar al primero {time} minutos")
