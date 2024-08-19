from random import randint

from brain_games.game import NO, YES

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num) -> bool:
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def get_question_and_right_answer() -> list:
    guess_num = randint(1, 1000)
    right_answer = YES if is_prime(guess_num) else NO
    question = f"Question: {guess_num}"
    return question, right_answer
