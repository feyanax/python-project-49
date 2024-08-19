from math import gcd
from random import randint

RULES = "Find the greatest common divisor of given numbers."


def get_question_and_right_answer() -> list:
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = f"Question: {first_num} {second_num}"
    right_answer = gcd(first_num, second_num)
    return question, str(right_answer)
