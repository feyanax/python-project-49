from math import gcd
from random import randint

RULES = "Find the greatest common divisor of given numbers."


def game_logic() -> list:
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    print(f"Question: {first_num} {second_num}")
    user_answer = input("Your answer: ")
    correct_answer = gcd(first_num, second_num)
    return [user_answer, str(correct_answer)]
