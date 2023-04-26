"""
            Segunda versión. Las preguntas están almacenas en un fichero de preguntas.
            Cada pregunta está separada de la siguiente con una línea cuyo valor es “---”.

    Autor: Angel Fernandez Ariza
"""
from Ejercicios.Autotest.pt2.question import Question


def main():
    with open("preguntas.txt", 'r', encoding='utf-8') as questions_chain:
        get_questions = questions_chain.read()
    broker = "---"
    num_questions = get_questions.count(broker)

    with open("preguntas.txt", 'r', encoding='utf-8') as questions:
        file = questions.readlines()

    file = [line.strip() for line in file]

    question_counter = 0
    while question_counter < num_questions:
        questions_list = []
        for j in file:
            if j == broker:
                break
            questions_list.append(j)
        title = questions_list.pop(0)
        enum = ""
        delete_counter = 0
        for i in range(len(questions_list)):
            if questions_list[i] == ".":
                delete_counter = i + 1
                break
            enum += questions_list[i]
        for k in range(delete_counter):
            questions_list.remove(questions_list[0])

        options = ([(questions_list[0], float(questions_list[1])), (questions_list[2], float(questions_list[3])), (questions_list[4], float(questions_list[5])), (questions_list[6], float(questions_list[7]))])
        question = Question(title, enum, options, 1)
        question.print_question()
        question.user_answer()
        question_counter += 1
        delete_counter2 = 0
        for l in range(len(file)):
            if file[l] == broker:
                delete_counter2 = l + 1
                break
        for k in range(delete_counter2):
            file.remove(file[0])

if __name__ == '__main__':
    main()
