from random import randint

import prompt

YES = "yes"
NO = "no"
ERROR_MESSAGE = "'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
WIN_MESSAGE = "Congratulations, {name}!"
CORRECT = "Correct!"
ATTEMPTS_NUM = 3


def isEven(num: int) -> bool:
    return num % 2 == 0


def game_logic(name: str) -> None:
    for attempt in range(ATTEMPTS_NUM):
        mystery_num = randint(1, 300)
        print(f"Question: {mystery_num}")
        user_answer = input("Your answer: ")
        correct_answer = YES if isEven(mystery_num) else NO
        if user_answer == correct_answer:
            print(CORRECT)
        else:
            print(
                ERROR_MESSAGE.format(
                    user_answer=user_answer, correct_answer=correct_answer, name=name
                )
            )
            return
    print(WIN_MESSAGE.format(name=name))


def main() -> None:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_logic(name)


if __name__ == "__main__":
    main()
