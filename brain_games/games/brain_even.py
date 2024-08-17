from random import randint

YES = "yes"
NO = "no"
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def isEven(num: int) -> bool:
    return num % 2 == 0


def game_logic():
    guess_num = randint(1, 301)
    correct_answer = YES if isEven(guess_num) else NO
    print(f"Question: {guess_num}")
    user_answer = input("Your answer: ")
    return [user_answer, correct_answer]
