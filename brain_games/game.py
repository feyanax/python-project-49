import prompt

ERROR_MESSAGE = (
    "'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
    ".\nLet's try again, {name}!"
)
WIN_MESSAGE = "Congratulations, {name}!"
CORRECT = "Correct!"
ATTEMPTS_NUM = 3


def game_greet(game_rules: str) -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(game_rules)
    return name


def run_game(game) -> None:
    name = game_greet(game.RULES)

    for attempt in range(ATTEMPTS_NUM):
        [user_answer, correct_answer] = game.game_logic()
        if user_answer == correct_answer:
            print(CORRECT)
            continue
        else:
            print(
                ERROR_MESSAGE.format(
                    user_answer=user_answer,
                    correct_answer=correct_answer,
                    name=name,
                )
            )
            return

    print(WIN_MESSAGE.format(name=name))
