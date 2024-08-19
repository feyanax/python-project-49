from random import randint

RULES = "What number is missing in the progression?"


def get_question_and_right_answer() -> list:
    progression_length = randint(5, 15)
    first_num = randint(2, 100)
    step_num = randint(2, 9)
    progression = []

    for i in range(progression_length):
        second_num = first_num + step_num
        first_num = second_num
        progression.append(str(second_num))

    guess_num_index = randint(2, len(progression) - 1)
    right_answer = progression[guess_num_index]
    progression[guess_num_index] = ".."
    question = f"Question: {' '.join(progression)}"
    return question, right_answer
