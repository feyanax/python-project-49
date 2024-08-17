from random import randint

from brain_games.game import run_game

YES = "yes"
NO = "no"


def isEven(num: int) -> bool:
    return num % 2 == 0


def game_logic():
    guess_num = randint(1, 301)
    correct_answer = YES if isEven(guess_num) else NO
    print(f"Question: {guess_num}")
    user_answer = input("Your answer: ")
    return [user_answer, correct_answer]


def main() -> None:
    run_game(
        rules='Answer "yes" if the number is even, otherwise answer "no".',
        game_logic=game_logic,
    )


if __name__ == "__main__":
    main()
