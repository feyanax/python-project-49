from random import randint

from brain_games.game import NO, YES

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(num) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
        return True


def game_logic() -> list:
    guess_num = randint(1, 1000)
    correct_answer = YES if isPrime(guess_num) else NO
    print(f"Question: {guess_num}")
    user_answer = input("Your answer: ")
    return [user_answer, correct_answer]
