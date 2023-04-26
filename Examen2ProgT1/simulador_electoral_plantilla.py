"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.
"""
from utilities import menu

MIN_PERCENT_VOTES = 0.05

city = None
valid_votes = 0
seats = 0
votes_parties = []

def main():
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()
        elif option == 2:
            input_electoral_data()
        elif option == 3:
            input_party_votes()
        elif option == 4:
            print_simulation()
        else:
            break
        print()

    print("¡Hasta la próxima! ;-)")


def load_electoral_data_cordova():
    global city, valid_votes, seats, votes_parties
    city = "CÓRDOBA"
    valid_votes = 146548
    seats = 29
    votes_parties = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                     [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                     [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                     [161, "PUM+J"]]
    print("Datos de Córdoba cargados.")

def input_electoral_data():
    global city, valid_votes, seats
    consent = None
    if city == "CÓRDOBA":
        consent = input("Esto implica borrar los datos ya introducidos. Responda 'Sí' para prodecer: ")
    if consent == "Sí" or "Si" or not None:
        city = input("Introduce un municipio: ")
        valid_votes = input("Introduce número de votos válidos: ")
        seats = input("Introduce un número de ediles: ")
    print()
    print(f"Datos de {city} cargados.")

def input_party_votes():
    global city, valid_votes, seats, votes_parties
    partidos = [["PP"], ["PSOE"], ["Ciudadanos"], ["IU ANDALUCÍA"],
                ["VOX"], ["PODEMOS"], ["PACMA"], ["ACCIÓN POR CÓRDOBA"],
                ["PCTE"], ["ANDALUCÍA ENTRE TOD@S"], ["GANEMOS"], ["EB"],
                ["PUM+J"]]
    contador = 0
    for i in range(len(partidos)):
        print(f"Partido político: {partidos[i]}")
        votes = int(input(f"Cuantos votos tiene {partidos[i]}: "))
        votes += votes
        if votes == valid_votes:
            break
        partidos[i].append(str(votes))


def print_simulation():
    pass



def seats_with_dhont():
    pass


if __name__ == "__main__":
    main()

