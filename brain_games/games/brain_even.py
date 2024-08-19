from random import randint

from brain_games.game import NO, YES

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_question_and_right_answer() -> list:
    guess_num = randint(1, 301)
    right_answer = YES if is_even(guess_num) else NO
    question = f"Question: {guess_num}"
    return question, right_answer
