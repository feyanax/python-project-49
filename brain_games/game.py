import prompt

ERROR_MESSAGE = (
    "'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
    ".\nLet's try again, {name}!"
)
WIN_MESSAGE = "Congratulations, {name}!"
CORRECT = "Correct!"
ATTEMPTS_NUM = 3
YES = "yes"
NO = "no"


def game_greet() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def run_game(game) -> None:
    name = game_greet()
    print(game.RULES)

    for attempt in range(ATTEMPTS_NUM):
        question, right_answer = game.game_logic()
        print(question)
        user_answer = input("Your answer: ")
        if user_answer == right_answer:
            print(CORRECT)
            continue
        else:
            print(
                ERROR_MESSAGE.format(
                    user_answer=user_answer,
                    correct_answer=right_answer,
                    name=name,
                )
            )
            return

    print(WIN_MESSAGE.format(name=name))
