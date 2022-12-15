import random


QUESTION = 'What is the result of the expression?'


def get_expression_result(number1, number2, expression):
    result = 0
    if expression == '+':
        result = number1 + number2
    elif expression == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return result


def build_game():
    # Инициализируем два случайных номера и случайное математическое выражение
    random_number_1 = random.randint(1, 99)
    random_number_2 = random.randint(1, 99)
    random_expression = random.choice('+-*')
    # Передаем данные в get_expression_result чтобы получить результат выражения
    result = get_expression_result(
        random_number_1, random_number_2, random_expression
    )
    question = str(
        f'Question: {random_number_1} {random_expression} {random_number_2}'
    )
    return str(result), question
