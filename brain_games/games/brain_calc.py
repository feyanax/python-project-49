from random import choice, randint

RULES = "What is the result of the expression?"


def get_question_and_right_answer() -> list:
    left_operand = randint(1, 100)
    right_operand = randint(1, 100)
    operator = choice(["+", "-", "*"])
    question = f"Question: {left_operand} {operator} {right_operand}"

    match operator:
        case "+":
            right_answer = left_operand + right_operand
        case "-":
            right_answer = left_operand - right_operand
        case "*":
            right_answer = left_operand * right_operand

    return question, str(right_answer)
