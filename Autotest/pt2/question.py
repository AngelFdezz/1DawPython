"""
        Ejercicio Autotest V1:

            Se pretende crear una aplicación que haga exámenes tipo test similares a como los realiza la
            plataforma Moodle con una sola respuesta. Esta plataforma permite crear un cuestionario, añadirle
            preguntas, ejecutarlo y dar una calificación

    Autor: Angel Fernández Ariza
    Curso: 2022-2023
"""
from typeguard import typechecked


class Answer_not_found(ValueError):
    def __init__(self):
        super().__init__(f"La respuesta introducida no coincide con ninguna de las posibles elecciones.")


@typechecked
class Question:
    __counter_questions = 0

    def __init__(self, name: str, enum: str, options: list[tuple[str, float]], base_score: float = 1):
        self.__name = name
        self.__enum = enum
        self.__options = options
        self.__base_score = base_score
        Question.__counter_questions += 1

    @property
    def name(self):
        return self.__name

    @property
    def enum(self):
        return self.__enum

    @property
    def options(self):
        return self.__options

    @property
    def base_score(self):
        return self.__base_score

    @property
    def user_score(self):
        return self.__user_score

    def print_question(self):
        print(f"------------------------------------------------")
        print(f"Pregunta {Question.__counter_questions}:")
        print(f"{self.__enum}")
        print("")
        print(f"Opciones:")
        print("")
        for choice in self.__options:
            print(f"* {choice[0]}")

    def user_answer(self):
        answer = input("¿Cuál es la respuesta correcta?:     ")
        options_choices = []
        for i in self.__options:
            options_choices.append(i[0])
        if answer not in options_choices and answer != "":
            raise Answer_not_found()
        elif answer == "":
            user_score = 0
            self.print_user_score(user_score)
        else:
            user_score = self.get_score_question(options_choices, answer)
            self.print_user_score(user_score)

    @staticmethod
    def print_user_score(user_score):
        print(f"Puntuación obtenida: {user_score}")

    def get_score_question(self, options_choices, answer):
        correct_answer = 0
        for j in range(len(options_choices)):
            if options_choices[j] == answer:
                correct_answer = j
        options_points = []
        for i in self.__options:
            options_points.append(i[1])
        return self.__base_score * options_points[correct_answer]
