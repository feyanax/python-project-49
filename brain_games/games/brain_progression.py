from random import randint

RULES = "What number is missing in the progression?"


def game_logic() -> list:
    progression_length = randint(5, 15)
    first_num = randint(2, 100)
    step_num = randint(2, 9)
    progression = []

    for i in range(progression_length):
        second_num = first_num + step_num
        first_num = second_num
        progression.append(str(second_num))

    guess_num_index = randint(2, len(progression) - 1)
    correct_answer = progression[guess_num_index]
    progression[guess_num_index] = ".."
    print(f"Question: {' '.join(progression)}")
    user_answer = input("Your answer: ")
    return [user_answer, correct_answer]
