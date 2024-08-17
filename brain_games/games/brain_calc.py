from random import choice, randint

RULES = "What is the result of the expression?"


def game_logic() -> list:
    left_operand = randint(1, 100)
    right_operand = randint(1, 100)
    operator = choice(["+", "-", "*"])
    print(f"Question: {left_operand}{operator}{right_operand}")
    user_answer = input("Your answer: ")

    match operator:
        case "+":
            correct_answer = left_operand + right_operand
        case "-":
            correct_answer = left_operand - right_operand
        case "*":
            correct_answer = left_operand * right_operand

    return [user_answer, str(correct_answer)]
