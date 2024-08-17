from random import randint

from brain_games.game import NO, YES

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(num) -> bool:
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def game_logic() -> list:
    guess_num = randint(1, 1000)
    correct_answer = YES if isPrime(guess_num) else NO
    print(f"Question: {guess_num}")
    user_answer = input("Your answer: ")
    return [user_answer, correct_answer]
